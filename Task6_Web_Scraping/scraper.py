import requests
from bs4 import BeautifulSoup
import textwrap

# ==========================================
# ETHICAL WEB SCRAPING GUIDELINES
# 1. Respect Terms of Service (ToS) and robots.txt.
# 2. Do not overload the server; avoid excessive requests in a short time.
# 3. Only scrape publicly available, non-sensitive data.
# 4. Always identify your scraper using a custom User-Agent.
# ==========================================

# Custom headers to identify the request
HEADERS = {
    'User-Agent': 'Python Interactive Educational Scraper bot/1.0 (Learning Project)'
}

def fetch_html(url):
    """
    Fetches the HTML content of a given URL.
    Handles network errors, timeouts, and invalid URLs gracefully.
    """
    try:
        # Timeout set to 5 seconds to prevent hanging
        response = requests.get(url, headers=HEADERS, timeout=5)
        # Raise an exception for bad HTTP status codes (e.g., 404, 500)
        response.raise_for_status()
        return response.text
    except requests.exceptions.MissingSchema:
        print("\n[Error] Invalid URL format. Please include 'http://' or 'https://'.")
    except requests.exceptions.ConnectionError:
        print("\n[Error] Failed to connect. Please check your internet or the URL.")
    except requests.exceptions.Timeout:
        print("\n[Error] The request timed out. The server took too long to respond.")
    except requests.exceptions.HTTPError as err:
        print(f"\n[Error] HTTP Error occurred: {err}")
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred: {e}")
    
    return None

def scrape_title(soup):
    """Extracts and prints the page title."""
    print("\n--- Page Title ---")
    title = soup.title
    if title and title.string:
        print(title.string.strip())
    else:
        print("No title found.")

def scrape_headings(soup):
    """Extracts and prints h1, h2, and h3 headings."""
    print("\n--- Headings (h1, h2, h3) ---")
    headings = soup.find_all(['h1', 'h2', 'h3'])
    if not headings:
        print("No headings found.")
        return
    
    for tag in headings:
        # Using get_text(strip=True) to clean up internal whitespace/newlines
        text = tag.get_text(strip=True)
        if text:
            print(f"[{tag.name.upper()}] {text}")

def scrape_paragraphs(soup):
    """Extracts and prints paragraphs, truncating long text."""
    print("\n--- Paragraphs ---")
    paragraphs = soup.find_all('p')
    if not paragraphs:
        print("No paragraphs found.")
        return
    
    for i, p in enumerate(paragraphs, 1):
        text = p.get_text(strip=True)
        if text:
            # Truncate text longer than 150 characters for readability
            short_text = textwrap.shorten(text, width=150, placeholder="...")
            print(f"{i}. {short_text}")

def scrape_links(soup):
    """Extracts and prints hyperkinks (first 15 to avoid clutter)."""
    print("\n--- Links (First 15) ---")
    links = soup.find_all('a', href=True)
    if not links:
        print("No links found.")
        return
    
    for i, link in enumerate(links[:15], 1):
        text = link.get_text(strip=True) or "No Text"
        href = link['href']
        print(f"{i}. {text} -> {href}")

def display_menu():
    """Displays the interactive menu options."""
    print("\n===============================")
    print("   What would you like to scrape?")
    print("===============================")
    print("1. Page Title")
    print("2. Headings (H1, H2, H3)")
    print("3. Paragraphs")
    print("4. Links")
    print("5. All Data")
    print("6. Enter a New URL")
    print("7. Exit")
    print("===============================")

def main():
    print("Welcome to the Interactive Web Scraper!")
    
    while True:
        url = input("\nEnter a website URL (e.g., https://example.com) or 'q' to quit: ").strip()
        if url.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        
        print(f"\nFetching data from {url}...")
        html_content = fetch_html(url)
        
        if not html_content:
            continue # Skip to the next iteration if fetching failed
            
        # Parse the HTML content once
        soup = BeautifulSoup(html_content, 'html.parser')
        print("Page parsed successfully!")
        
        while True:
            display_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                scrape_title(soup)
            elif choice == '2':
                scrape_headings(soup)
            elif choice == '3':
                scrape_paragraphs(soup)
            elif choice == '4':
                scrape_links(soup)
            elif choice == '5':
                scrape_title(soup)
                scrape_headings(soup)
                scrape_paragraphs(soup)
                scrape_links(soup)
            elif choice == '6':
                break # Break inner loop to ask for a new URL
            elif choice == '7':
                print("Exiting program. Goodbye!")
                return # Exit the entire script
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()