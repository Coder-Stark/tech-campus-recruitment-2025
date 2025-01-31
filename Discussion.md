# Discussion

## Solutions Considered

I explored several approaches for efficiently extracting logs for a given date from a large log file:

1. **Indexing Approach**: One approach I considered was creating an index for each date, where each log entry would be indexed by its date. This would allow direct access to logs for a specific date. However, this would require extra space to store the index, and the initial setup would be time-consuming, especially for a file as large as 1 TB.
   
2. **Line-by-Line Reading**: Another approach was reading the file line by line and filtering out entries that match the desired date. This approach is simple, memory-efficient, and doesn't require preprocessing the entire file. I chose this approach because it allows the program to handle extremely large files without consuming excessive memory.

## Final Solution Summary

After evaluating both approaches, I decided to use the **line-by-line reading** method. This approach is optimal for the following reasons:
- **Memory Efficiency**: The program reads one line at a time, which is crucial for handling large files (around 1 TB). Only matching lines are written to the output file, minimizing memory usage.
- **Simplicity**: The implementation is simple and does not require complex data structures like indexes.
- **Speed**: The program uses efficient string comparison (`find()` function) to check if a line starts with the target date, making it fast for date-based filtering.

## Steps to Run

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/Coder-Stark/tech-campus-recruitment-2025.git
