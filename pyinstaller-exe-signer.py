import random
import string
from datetime import datetime

def generate_random_version():
    """Generate a random version number in format X.Y.Z.W"""
    return (
        random.randint(1, 5),      # Major version
        random.randint(0, 9),      # Minor version
        random.randint(0, 9),      # Patch version
        random.randint(0, 9999)    # Build number
    )

def generate_random_company():
    """Generate a random company name"""
    prefixes = ["Cyber", "Digital", "Quantum", "Nexus", "Apex", "Omega", "Prime", "Elite"]
    suffixes = ["Solutions", "Systems", "Technologies", "Labs", "Dynamics", "Works", "Corp", "Inc"]
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

def generate_random_description():
    """Generate a random product description"""
    adjectives = ["Advanced", "Professional", "Enterprise", "Secure", "Optimized", "Next-Gen"]
    nouns = ["Scanner", "Analyzer", "Toolkit", "Framework", "Platform", "Suite"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def generate_random_name():
    """Generate a random product name"""
    tech_names = ["Crocell", "Nexus", "Quantum", "Cypher", "Titan", "Vortex", "Phoenix"]
    return random.choice(tech_names)

def generate_version_file():
    """Generate a complete version file with random information"""
    version = generate_random_version()
    company = generate_random_company()
    description = generate_random_description()
    product_name = generate_random_name()
    current_year = datetime.now().year
    
    version_content = f"""VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={version},
    prodvers={version},
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          u'040904B0',
          [StringStruct(u'CompanyName', u'{company}'),
           StringStruct(u'FileDescription', u'{description}'),
           StringStruct(u'FileVersion', u'{".".join(map(str, version))}'),
           StringStruct(u'InternalName', u'{product_name}'),
           StringStruct(u'LegalCopyright', u'Copyright © {current_year} {company}'),
           StringStruct(u'OriginalFilename', u'{product_name}.exe'),
           StringStruct(u'ProductName', u'{product_name}'),
           StringStruct(u'ProductVersion', u'{".".join(map(str, version))}')])
      ])
  ]
)"""
    
    return version_content

if __name__ == "__main__":
    # Generate the version file content
    version_content = generate_version_file()
    
    # Write to version.txt
    with open("version.txt", "w", encoding="utf-8") as f:
        f.write(version_content)
    
    print("✅ Random version file generated successfully!")
    print("📄 File saved as: version.txt")
    print("\nPreview of generated version info:")
    print("=" * 50)
    print(version_content)
    print("=" * 50)
