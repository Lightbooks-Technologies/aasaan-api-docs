import os

# Define the structure of the documentation as per the given JSON
doc_structure = [
   {
        "group": "Analytics",
        "pages": [
            "Bing Webmaster",
            "Clarity by Microsoft",
            "Google Analytics",
            "Hotjar",
            "Lucky Orange Analytics",
            "Meta Pixel"
        ]
    },
    {
        "group": "Shopping",
        "pages": [
            "Facebook Shop",
            "Google Shopping"
        ]
    },
   {
        "group": "Shipping",
        "pages": [
            "Borzo",
            "Delhivery",
            "iThink Logistics",
            "Pickrr",
            "Shiprocket",
            "Shipstation"
        ]
    },
   {
        "group": "Payments",
        "pages": [
            "aasaan Pay",
            "Paypal",
            "PayU",
            "Razorpay",
            "Stripe"
        ]
    },
   {
        "group": "Verify",
        "pages": [
            "Facebook Domain Verification",
            "Google Search Console"
        ]
    },
    {
        "group": "Migration",
        "pages": [
            "Magento",
            "Shopify",
            "WooCommerce"
        ]
    },
    {
        "group": "Google Search Console",
        "pages": [
            "Submit your Sitemap",
            "Request Indexing",
            "Important Notes"
        ]
    },
   {
        "group": "Support",
        "pages": [
            "Drift chat",
            "Freshchat",
            "Intercom",
            "Jivochat",
            "Kommunicate Chatbot, Live Chat",
            "LiveChat",
            "Richpanel Live Chat",
            "Tawk Chat",
            "Tidio Live Chat",
            "Userlike: Live Chat",
            "Zendesk Chat",
            "Zoho Chat"
        ]
    },
    {
        "group": "Communication",
        "pages": [
            "MSG91",
            "SendGrid",
            "WhatsApp White Label"
        ]
    },
    {
        "group": "Marketing",
        "pages": [
            "Adroll",
            "Ecomail",
            "Fomo",
            "Mailchimp",
            "Mailmunch",
            "Nudgify",
            "Optimonk",
            "Optinmonster",
            "Poptin",
            "Popupsmart",
            "Privy",
            "Wheelofpopups",
            "Wisepops",
            "Zotabox"
        ]
    }
]

# Function to create the directory structure and markdown files
def create_docs(base_path, structure):
    os.makedirs(base_path, exist_ok=True)  # Ensure the base directory exists

    for group in structure:
        # Create a directory for the group
        group_dir = os.path.join(base_path, group['group'].replace(" ", "-").lower())
        os.makedirs(group_dir, exist_ok=True)

        for page in group['pages']:
            # Replace spaces and slashes in page names with dashes for file names and subdirectories
            page_file_name = page.replace(" ", "-").replace("/", "-").lower() + ".mdx"
            md_file_path = os.path.join(group_dir, page_file_name)

            # Write content to the markdown file
            with open(md_file_path, 'w') as md_file:
                md_file.write(f"# {page}\n\nContent for {page} goes here.")

# Assuming '/mnt/data/docs' is your desired base directory
base_path = '/Users/sivaramrajugadiraju/Documents/Documents-sivaramMacBookPro/aasaan-api-docs/documentation/app-market'

# Run the function to create the documentation structure
create_docs(base_path, doc_structure)

print(f"Documentation structure created at {base_path}")
