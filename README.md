# Department of \***\*\_\*\***

Team Members:

- Cheryl Chen
- Maisha Supritee Chowdhury
- Maria Kapitanenko
- Sophia Don Tranho
- Tran Nguyen

# Setting up Environment

### ** Create a virtual environment in this project folder**

Open the terminal and follow the code below:

```bash
# To create a virtual environment named venv
python -m venv ./venv
```

```bash
# To run the virtual environment whenever you are coding
.\venv\Scripts\activate
```

### Install the following packages

- pandas
- numpy
- scipy
- matplotlib
- seaborn

To install all the packages using terminal:

```bash
pip install -r requirements.txt
```

# Website

The website is in the website directory. Make sure you have node.js installed.

### Website Setup
When you first download the website, run `npm install` to download the node_modules folder.

### Run Website Server

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.