#string analysis turotial, analyse URL's and asset ID's 
def analyse_url(url: str) -> None:
    #analyse information contained in a URL 
    print("\n--- URL Analysis ---")
    print(f"URL: {url}")

    #check the start of the URL
    if url.startswith("https://"):
        print("HTTPS detected - connection is encrypted.")
    elif url[0:4] == "http":
        print("HTTP detected - connection is not encrypted.")
    else:
        print("URL protocol not recognised")

    # check for text within the URL 
    if "admin" in url:
        print("Admin area detected.")
#check if URL ends with doc
    if url.endswith("docs"):
        print("Documentation page detected.")
    else:
        print ("No documentation detected.")


def analyse_asset(asset_id: str) -> tuple[str, str, str]:
#analyse an asset ID and return its seperate parts

    print("\n---Asset Analysis ---")
    print(f"Asset ID: {asset_id}")
#split the asset ID into seperate parts 
    parts = asset_id.split("-")

    asset_type = parts[0]
    asset_number= parts[1]
    asset_location = parts[2].upper()

    if asset_number.isdigit():
        print("Asset number is numeric.")
    else:
        print("Asset number is not numeric.")
    return asset_type, asset_number, asset_location


def main() -> None:
    #run the program

    url = input ("Enter a URL")
    asset_id = input ("Enter ID")
    analyse_url(url)
    asset_type, asset_number, asset_location = analyse_asset(asset_id)
    print(f"asset type: {asset_type}")
    print(f"asset number: {asset_number}")
    print(f"asset location: {asset_location}")
if __name__ == "__main__":
    main()



