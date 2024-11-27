# Setup for data generation scripts

1. Clone the program's repository onto your machine: https://github.com/makersacademy/extending-testing-resources/tree/main
2. Using the terminal, navigate into the repository's root directory
3. Run `cd unit2/03_resources` to navigate to the program's source code
4. Create a virtual environment by running `python -m venv _venv`
5. Activate the virtual environment by running `source _venv/bin/activate`
6. Install the Faker dependency by running `pip install Faker`
7. Run `touch generate-test-data.py run-data-generation.zsh`
8. Alongside the 'scripts/setup.md' file you are reading right now, you will find 'scripts/generate-test-data.py' and 'scripts/run-data-generation.zsh'. Copy the contents of these files into the corresponding files that you have just created in the program's repository.
9. Make the 'run-data-generation.zsh' script executable by running `chmod +x run-data-generation.zsh`
10. Execute the data generation script by running `./run-data-generation.zsh`. This will create 10 files inside the 'originals' folder. 

## Usage guide
- You can specify the number of files to create by adjusting the 'count' variable on Line 1 of 'run-data-generation.zsh'.
- To create new files for folders other than 'originals', replace the word 'originals' with the name of your chosen folder (Line 4 of run-data-generation.zsh'). This can be used to add files to 'updates' or 'finals'.
