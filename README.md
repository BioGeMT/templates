# templates
 Coding Templates and Best Practices

# Best Practices

1. **One Script, one job!** --- keep it contained as much as possible. It is better to string multiple scripts one after the other (more modular / easier to change) than to make a gigantic script that does everything.
2. **Make the names count.** Be as specific as you can. Does your script work for only a specific file type? explicitly state that up top. Talk to someone before you name reusable scripts.
3. Arguments **in/out** -
    3a. Never hardcode filenames
    3b. Always allow STDIN / STDOUT access for simple scripts with 1 main input and output
    3c. Define what the arguments are explicitly. Nobody will remember this in 5 years.
4. **Tests.** Even if it is a simple file and a command to run it and see that the result is the same. A simple test like that can save days of debugging in the future. Pay it forward! Write that test before you start.
