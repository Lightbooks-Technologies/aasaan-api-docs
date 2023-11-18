import os

# Define the structure of the documentation as per the given JSON
doc_structure = [
    
    {
        "group": "Fundamentals",
        "pages": ["Getting set up"]
    },
    {
        "group": "STOREFRONT",
        "pages": [
            "Design",
            "SEO",
            "Domain",
            "Social Media",
            "About Us",
            "Store Policies",
            "Blogs",
            "QR Code",
            "Place Order",
            "Mobile App"
        ]
    },
    {
        "group": "COMMERCE",
        "pages": [
            "Brands",
            "Categories",
            "Products",
            "Orders",
            "Customers",
            "Store Settings",
            "Warehouses",
            "Manage Staff",
            "Custom Fields",
            "KYC",
            "Coupons",
            "Channels"
        ]
    },
    {
        "group": "APP MARKET",
        "pages": [
            "Introduction to the App Market",
            "Analytics",
            "Shopping",
            "Shipping",
            "Payments",
            "Verify",
            "Migration",
            "Support",
            "Communication",
            "Marketing"
        ]
    },
    {
        "group": "ACCOUNT",
        "pages": ["Manage Account", "How to Subscribe"]
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
base_path = '/Users/sivaramrajugadiraju/Documents/Documents-sivaramMacBookPro/aasaan-api-docs/documentation'

# Run the function to create the documentation structure
create_docs(base_path, doc_structure)

print(f"Documentation structure created at {base_path}")
