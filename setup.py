from setuptools import setup, find_packages

setup(
    name="gitsmart",
    version="1.0.0",
    description="AI-Powered Git Commit Assistant",
    author="Andrew Clark",
    packages=find_packages(),  # or ["GitSmart"] if you prefer explicitly
    install_requires=[
        "questionary>=1.10.0",
        "rich>=13.0.0",
        "requests>=2.28.0",
        "prompt_toolkit>=3.0.0",
        "pytest",
        "count-tokens",
        "diskcache",
        "flask>=2.0.0",
        "flask-cors>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "gitsmart = GitSmart.main:entry_point",
            # The left side is the CLI command, the right side is
            # "package.module:function" for your main script
        ]
    },
    python_requires=">=3.7"
)
