from setuptools import setup,find_packages
HYPHEN_E_DOT="-e ."

def get_requirements():
    with open("requirements.txt","r") as file:
        requirements=file.readlines()
        requirements=[req for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="ner-using-bert",
    vrsion="0.0.1",
    author="Linkan Kumar Sahu",
    author_email="sahulinkan7@gmil.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

