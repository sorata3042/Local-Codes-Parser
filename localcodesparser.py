#Steven Chau

################################################################################

def main():
"""
Goes through localcodes.txt and removes superflous stuff from each line.
Creates a new textfile to for the updated information
"""
    with open("localcodes.txt", mode = "r") as txt_file:
        with open('localcodes-edited.txt', mode='w', newline = '') as file:
            for row in txt_file:
                row = row[:7]
                row.split(;, 1)
                file.writerow(row.split(;, 2))

################################################################################

main()
