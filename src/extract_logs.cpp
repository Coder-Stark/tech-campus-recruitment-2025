#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <sstream>

namespace fs = std::filesystem;

void extract_logs(const std::string &log_file, const std::string &target_date) {
    // Ensure the output directory exists
    std::string output_dir = "output";
    if (!fs::exists(output_dir)) {
        fs::create_directory(output_dir);
    }
    
    std::string output_file = output_dir + "/output_" + target_date + ".txt";

    // Open the log file for reading
    std::ifstream infile(log_file);
    if (!infile) {
        std::cerr << "Error: Unable to open log file: " << log_file << std::endl;
        return;
    }

    // Open the output file for writing
    std::ofstream outfile(output_file);
    if (!outfile) {
        std::cerr << "Error: Unable to create output file: " << output_file << std::endl;
        return;
    }

    std::string line;
    while (std::getline(infile, line)) {
        // Check if the line starts with the target date
        if (line.find(target_date) == 0) {
            outfile << line << "\n";
        }
    }

    infile.close();
    outfile.close();

    std::cout << "Logs for " << target_date << " saved to " << output_file << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: ./extract_logs <YYYY-MM-DD>" << std::endl;
        return 1;
    }

    std::string log_filename = "logs_2024.log"
    extract_logs(log_filename, argv[1]);

    return 0;
}
