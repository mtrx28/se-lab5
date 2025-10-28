### 1. Which issues were the easiest to fix, and which were the hardest? Why?
#### The easiest issues to fix were the line length errors (E501) and trailing whitespace. They just needed minor formatting adjustments like breaking long lines or deleting extra spaces. Whereas the hardest was converting the naming convention of the functions to snake_case because they required changing function names everywhere in the code, which could easily cause errors if I missed updating a reference.

### 2. Did the static analysis tools report any false positives? If so, describe one example.
#### Yes, there was a mild false positive, the tool flagged the use of the global statement in an earlier version of the code as bad practice, even though it was being used safely for maintaining shared state. So while technically valid, it wasn’t really an issue in that small context.

### 3. How would you integrate static analysis tools into your actual software development workflow?
#### I would integrate them into my CI/CD pipeline so that every time code is pushed to GitHub, the analysis runs automatically and reports issues. For local development, I’d use a pre-commit hook with tools like flake8 or pylint to catch basic formatting and logical issues before committing the code.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
#### After applying the fixes, the code looked cleaner, more consistent, and easier to read. Following snake_case naming made the functions more Pythonic, and fixing long lines improved readability. The structured logging and validation also made the code feel more reliable and maintainable.