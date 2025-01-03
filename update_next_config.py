import os
import sys

NEXT_CONFIG_PATH = ".web/next.config.js"


# New rewrite rule to insert
REWRITE_RULE = """
      {
        source: '/docsite',
        destination: '/docsite/index.html',
      }
"""
import sys



def update_next_config():
    try:
        # Read the file content
        with open(NEXT_CONFIG_PATH, "r") as f:
            content = f.read()

        # Debug: Print the original content for verification
        print("Original Content:")
        print(content)

        # Check if the rewrite rule already exists
        if "source: '/docsite'" in content:
            print("Rewrite rule already exists. No changes made.")
            return

        # Check if `async rewrites()` exists
        if "async rewrites()" in content:
            print("Found existing 'async rewrites()'. Appending new rule...")
            updated_content = content.replace(
                "return [", f"return [\n      {REWRITE_RULE},"
            )
        elif "const nextConfig = {" in content:
            # Add the `async rewrites()` section if it's missing
            print("Adding 'async rewrites()' section...")
            updated_content = content.replace(
                "const nextConfig = {",
                f"""
const nextConfig = {{
  async rewrites() {{
    return [
      {REWRITE_RULE}
    ];
  }},
""",
            )
        else:
            print("Could not find a suitable location to add the rewrite rule.")
            return

        # Debug: Print the updated content for verification
        print("Updated Content:")
        print(updated_content)

        # Write the updated content back to the file
        with open(NEXT_CONFIG_PATH, "w") as f:
            f.write(updated_content)

        print(f"Updated {NEXT_CONFIG_PATH} with the new rewrite rule.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
  update_next_config()


