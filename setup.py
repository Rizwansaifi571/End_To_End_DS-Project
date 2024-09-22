from setuptools import find_packages, setup

# Define a constant for editable package installation.
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list[str]:
    '''
    This function returns a list of requirements read from a given file.
    It removes any editable package specifier from the list.
    '''
    requirements = []  # Initialize an empty list to hold the requirements.

    # Open the specified requirements file and read its contents.
    with open(file_path) as file_obj:
        # Read all lines from the file and store them in the requirements list.
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement string.
        requirements = [req.replace('\n', "") for req in requirements]

        # If the editable package specifier is found, remove it from the list.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements  # Return the final list of requirements.

# Call the setup function to configure the package.
setup(
    name="End_TO_End_Project",  # Name of the package.
    version="0.0.1",  # Version of the package.
    author="Mohd Rizwan",  # Author of the package.
    author_email='rizwansaifi2614@gmail.com',  # Author's email.
    packages=find_packages(),  # Automatically find packages in the project.
    install_requires=get_requirements('requirements.txt')  # Install dependencies from the requirements file.
)
