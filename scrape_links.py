
import json
import requests
import os
import time
from urllib.parse import urlparse

# Set a descriptive User-Agent
HEADERS = {
    'User-Agent': 'Manus-AI-Scraper/1.0 (contact@example.com)'
}

# Max file size for download (50 MB)
MAX_FILE_SIZE = 50 * 1024 * 1024

# Dictionary to store robots.txt rules per domain
ROBOTS_TXT_RULES = {}

def get_robots_txt(domain):
    if domain not in ROBOTS_TXT_RULES:
        try:
            response = requests.get(f"https://{domain}/robots.txt", headers=HEADERS, timeout=5)
            if response.status_code == 200:
                ROBOTS_TXT_RULES[domain] = response.text
            else:
                ROBOTS_TXT_RULES[domain] = ""
        except requests.exceptions.RequestException:
            ROBOTS_TXT_RULES[domain] = ""
    return ROBOTS_TXT_RULES[domain]

def is_allowed_by_robots_txt(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    
    robots_content = get_robots_txt(domain)
    
    # Simple robots.txt parsing for Disallow rules
    for line in robots_content.splitlines():
        if line.startswith("Disallow:"):
            disallow_path = line.split(":")[1].strip()
            if disallow_path and path.startswith(disallow_path):
                return False
    return True

def process_link(link_url, source_page):
    link_info = {
        "url": link_url,
        "source_page": source_page,
        "http_status": None,
        "content_type": None,
        "notes": []
    }

    parsed_url = urlparse(link_url)
    domain = parsed_url.netloc

    if not is_allowed_by_robots_txt(link_url):
        link_info["notes"].append("Disallowed by robots.txt")
        return link_info

    try:
        # Throttle requests
        time.sleep(1) # 1 request per second per domain

        response = requests.head(link_url, headers=HEADERS, allow_redirects=True, timeout=10)
        link_info["http_status"] = response.status_code
        link_info["content_type"] = response.headers.get("Content-Type")
        content_length = int(response.headers.get("Content-Length", 0))

        if 200 <= response.status_code < 300:
            if "text/html" in link_info["content_type"]:
                # Check for login/paywall by looking at common keywords in a small chunk of content
                # This is a very basic check and might not be accurate for all cases
                try:
                    # Fetch a small portion of the content to check for login/paywall
                    content_response = requests.get(link_url, headers=HEADERS, stream=True, timeout=10)
                    content_response.raise_for_status()
                    first_chunk = content_response.iter_content(chunk_size=1024).__next__().decode("utf-8", errors="ignore").lower()
                    if "login" in first_chunk or "sign in" in first_chunk or "subscribe" in first_chunk or "paywall" in first_chunk:
                        link_info["notes"].append("Requires login/paywall")
                    content_response.close()
                except requests.exceptions.RequestException:
                    link_info["notes"].append("Could not check for login/paywall")

            if "application/pdf" in link_info["content_type"] and content_length <= MAX_FILE_SIZE:
                file_name = os.path.join("downloads", os.path.basename(parsed_url.path) or "downloaded_pdf.pdf")
                if not file_name.endswith(".pdf"):
                    file_name += ".pdf"
                with requests.get(link_url, headers=HEADERS, stream=True, timeout=30) as r:
                    r.raise_for_status()
                    with open(file_name, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                link_info["notes"].append(f"Downloaded PDF: {file_name}")
            elif "text/plain" in link_info["content_type"] and content_length <= MAX_FILE_SIZE:
                file_name = os.path.join("downloads", os.path.basename(parsed_url.path) or "downloaded_text.txt")
                if not file_name.endswith(".txt"):
                    file_name += ".txt"
                with requests.get(link_url, headers=HEADERS, stream=True, timeout=30) as r:
                    r.raise_for_status()
                    with open(file_name, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                link_info["notes"].append(f"Downloaded text file: {file_name}")
            elif content_length > MAX_FILE_SIZE:
                link_info["notes"].append("File too large to download")
        elif response.status_code >= 400:
            link_info["notes"].append(f"HTTP Error: {response.status_code}")

    except requests.exceptions.Timeout:
        link_info["notes"].append("Request timed out")
    except requests.exceptions.ConnectionError:
        link_info["notes"].append("Connection error")
    except requests.exceptions.RequestException as e:
        link_info["notes"].append(f"Request failed: {e}")
    
    return link_info


if __name__ == "__main__":
    # Links extracted from arxiv.org/abs/2212.06468
    arxiv_links = [
        # PDF link
        "https://arxiv.org/pdf/2212.06468",
        # Links from the abstract mentioning corpora availability
        # The abstract states: "The tool is open source, and the four corpora are also available online."
        # It also mentions ADAT (Arabic Dialect Annotation Toolkit) and Curras tagsets.
        # I need to infer potential dataset links from the text.
        # Searching for 



        # Based on the abstract, the corpora are available online and a tool called ADAT was developed.
        # I need to search for these terms on the page or related external links.
        # From the previous browser view, I saw 'Hugging Face' and 'Papers with Code' links under 'Code, Data, Media'.
        # These are likely candidates for hosting datasets or code.
        "https://huggingface.co/huggingface", # This is a general Hugging Face link, not specific to the paper
        "https://paperswithcode.com/", # This is a general Papers with Code link, not specific to the paper
        # The abstract mentions "Curras tagsets" and "SAMA". I will search for these terms on the page.
        # There is no direct link for the dataset or ADAT tool on the arXiv page.
        # I will add the Google Scholar link to see if there are other versions or links there.
        "https://scholar.google.com/scholar_lookup?arxiv_id=2212.06468"
    ]

    all_links_data = []

    for link in arxiv_links:
        print(f"Processing link: {link}")
        link_data = process_link(link, "https://arxiv.org/abs/2212.06468")
        all_links_data.append(link_data)

    # Save results to links.json
    with open("links.json", "w") as f:
        json.dump(all_links_data, f, indent=4)

    print("Scraping complete. Results saved to links.json")


