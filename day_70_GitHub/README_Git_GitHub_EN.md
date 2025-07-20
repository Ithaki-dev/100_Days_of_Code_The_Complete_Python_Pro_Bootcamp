# 📚 Git and GitHub - Version Control
*Class of July 19, 2025*

## 🎯 What are Git and GitHub?

**Git** is a distributed version control system that allows you to:
- Track changes in your code
- Collaborate with other developers
- Maintain a complete history of your project
- Revert changes when necessary

**GitHub** is a cloud platform that:
- Hosts Git repositories
- Facilitates collaboration
- Provides additional tools (Issues, Pull Requests, etc.)

---

## 🚀 Installing Git

### On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install git
```

### On macOS:
```bash
# With Homebrew
brew install git

# Or download from: https://git-scm.com/download/mac
```

### On Windows:
- Download from: https://git-scm.com/download/win
- Or use Windows Subsystem for Linux (WSL)

### Verify installation:
```bash
git --version
```

---

## ⚙️ Initial Configuration

```bash
# Configure your name and email (required)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Optional but useful configurations
git config --global init.defaultBranch main
git config --global core.editor "code --wait"  # For VS Code
```

---

## 📁 The Three States of Git

Git manages your files in three main states:

### 1. **Working Directory**
- Where you edit your files
- Changes not tracked by Git

### 2. **Staging Area**
- Files prepared for the next commit
- Like a "waiting area"

### 3. **Repository**
- Permanent commit history
- Where "snapshots" of your project are saved

```
Working Directory → Staging Area → Repository
     git add          git commit
```

---

## 🛠️ Basic Git Commands

### Initialize a repository:
```bash
git init
```

### Clone an existing repository:
```bash
git clone https://github.com/username/repository.git
git clone git@github.com:username/repository.git  # With SSH
```

### Check status:
```bash
git status
```

### Add files to staging area:
```bash
git add file.txt              # Add a specific file
git add .                     # Add all files
git add *.py                  # Add all .py files
```

### Make a commit:
```bash
git commit -m "Descriptive commit message"
git commit -am "Add and commit in one step"  # Only for already tracked files
```

### View history:
```bash
git log
git log --oneline             # Compact version
git log --graph --oneline     # With branch graph
```

### View differences:
```bash
git diff                      # Changes in working directory
git diff --staged             # Changes in staging area
git diff HEAD~1               # Compare with previous commit
```

### Working with branches:
```bash
git branch                    # List branches
git branch new-branch         # Create new branch
git checkout new-branch       # Switch to a branch
git checkout -b new-branch    # Create and switch in one step
git switch new-branch         # Modern command to switch branches
git switch -c new-branch      # Create and switch (modern)
```

### Synchronize with remote repository:
```bash
git remote -v                 # View remote repositories
git push origin main          # Upload changes
git pull origin main          # Download changes
git fetch                     # Download without merging
```

---

## 🍴 Fork and Pull Requests

### What is a Fork?
A **fork** is a copy of a repository in your GitHub account that allows you to:
- Experiment without affecting the original project
- Contribute to open source projects
- Propose changes to the original repository

### Fork and Pull Request Process:

#### 1. **Fork the repository**
- Go to the repository on GitHub
- Click the "Fork" button (🍴)
- A copy is created in your account

#### 2. **Clone your fork**
```bash
git clone https://github.com/YOUR_USERNAME/forked-repository.git
cd forked-repository
```

#### 3. **Configure the original repository as upstream**
```bash
git remote add upstream https://github.com/ORIGINAL_USER/original-repository.git
git remote -v  # Verify
```

#### 4. **Create a branch for your contribution**
```bash
git checkout -b my-new-feature
```

#### 5. **Make changes and commits**
```bash
# Edit files
git add .
git commit -m "Add new feature"
```

#### 6. **Push changes to your fork**
```bash
git push origin my-new-feature
```

#### 7. **Create Pull Request**
- Go to your fork on GitHub
- You'll see a "Compare & pull request" button
- Describe your changes
- Click "Create pull request"

#### 8. **Keep your fork updated**
```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

---

## 🔧 Additional Useful Commands

### Undo changes:
```bash
git restore file.txt          # Undo changes in working directory
git restore --staged file.txt # Remove from staging area
git reset HEAD~1              # Undo last commit (keep changes)
git reset --hard HEAD~1       # Undo last commit (DANGEROUS)
```

### Working with stash:
```bash
git stash                     # Save changes temporarily
git stash pop                 # Recover saved changes
git stash list                # View list of stashes
```

### Tags:
```bash
git tag v1.0                  # Create tag
git tag -a v1.0 -m "Version 1.0"  # Annotated tag
git push origin v1.0          # Push tag
```

---

## 📝 Best Practices

### ✅ **DO's**
- Write descriptive commit messages
- Make small and frequent commits
- Use branches for new features
- Update regularly from upstream
- Review changes before committing

### ❌ **DON'Ts**
- Make commits directly to `main` in collaborative projects
- Generic commit messages like "fix" or "update"
- Massive commits with many different changes
- Upload large or sensitive files (passwords, .env)
- Rewrite history on shared branches

---

## 🔍 Debugging Commands

```bash
# See who modified each line
git blame file.txt

# Search in history
git log --grep="bug"
git log -S "specific_function"

# View differences between branches
git diff main..new-branch

# View files in a specific commit
git show commit_hash:file.txt
```

---

## 📚 Typical Workflow

```bash
# 1. Update local repository
git pull origin main

# 2. Create new branch for feature
git checkout -b new-feature

# 3. Work on changes
# ... edit files ...

# 4. Add and commit
git add .
git commit -m "Implement new feature"

# 5. Push the branch
git push origin new-feature

# 6. Create Pull Request on GitHub

# 7. After approval, clean up
git checkout main
git pull origin main
git branch -d new-feature
```

---

## 🎯 .gitignore File

Create a `.gitignore` file to exclude files that shouldn't be versioned:

```gitignore
# Virtual environments
venv/
env/
.env

# Python cache
__pycache__/
*.pyc
*.pyo

# IDEs
.vscode/
.idea/
*.swp

# System files
.DS_Store
Thumbs.db

# Logs
*.log

# Dependencies
node_modules/
```

---

## 🚀 Additional Resources

- **Official Documentation**: https://git-scm.com/doc
- **GitHub Learning Lab**: https://github.com/apps/github-learning-lab
- **Visualizing Git**: http://git-school.github.io/visualizing-git/
- **Cheat Sheet**: https://training.github.com/downloads/github-git-cheat-sheet/

---

## 🏆 Summary of What We Learned Today

✅ **Git installation and configuration**  
✅ **The three states of Git (Working Directory, Staging Area, Repository)**  
✅ **Basic commands for daily workflow**  
✅ **How to clone repositories**  
✅ **Complete Fork and Pull Request process**  
✅ **Best practices and workflows**  

### 🎉 Now you can collaborate on projects and maintain professional version control!

---

*Made with ❤️ for the 100 Days of Code Python Bootcamp*
