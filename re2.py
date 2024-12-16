import datetime

def find_restriction_sites(dna_sequence):
    # Define restriction enzymes and their details
    enzymes = {
        "EcoRI": {"site": "GAATTC", "cut_type": "Sticky ends (5' overhang)"},
        "HindIII": {"site": "AAGCTT", "cut_type": "Sticky ends (5' overhang)"},
        "BamHI": {"site": "GGATCC", "cut_type": "Sticky ends (5' overhang)"},
        "PstI": {"site": "CTGCAG", "cut_type": "Sticky ends (3' overhang)"},
        "NotI": {"site": "GCGGCCGC", "cut_type": "Sticky ends (5' overhang)"},
        "XhoI": {"site": "CTCGAG", "cut_type": "Sticky ends (5' overhang)"},
        "SmaI": {"site": "CCCGGG", "cut_type": "Blunt ends"},
        "AluI": {"site": "AGCT", "cut_type": "Blunt ends"},
        "HaeIII": {"site": "GGCC", "cut_type": "Blunt ends"},
        "TaqI": {"site": "TCGA", "cut_type": "Sticky ends (5' overhang)"},
        "BglII": {"site": "AGATCT", "cut_type": "Sticky ends (5' overhang)"},
        "ApaI": {"site": "GGGCCC", "cut_type": "Sticky ends (3' overhang)"},
        "KpnI": {"site": "GGTACC", "cut_type": "Sticky ends (3' overhang)"},
        "ClaI": {"site": "ATCGAT", "cut_type": "Sticky ends (5' overhang)"},
        "SacI": {"site": "GAGCTC", "cut_type": "Sticky ends (5' overhang)"},
        "NcoI": {"site": "CCATGG", "cut_type": "Sticky ends (5' overhang)"},
        "SalI": {"site": "GTCGAC", "cut_type": "Sticky ends (5' overhang)"},
        "ScaI": {"site": "AGTACT", "cut_type": "Blunt ends"},
        "NheI": {"site": "GCTAGC", "cut_type": "Sticky ends (5' overhang)"},
        "EcoRV": {"site": "GATATC", "cut_type": "Blunt ends"},
        "XbaI": {"site": "TCTAGA", "cut_type": "Sticky ends (5' overhang)"},
        "HpaI": {"site": "GTTAAC", "cut_type": "Blunt ends"},
        "SphI": {"site": "GCATGC", "cut_type": "Sticky ends (5' overhang)"},
        "AvaI": {"site": "CYCGRG", "cut_type": "Sticky ends (5' overhang)"},
        "DpnI": {"site": "Gm6ATC", "cut_type": "Methylation-dependent cut"}
    }

    # Convert input sequence to uppercase
    dna_sequence = dna_sequence.upper()

    # Store results
    results = []

    for enzyme, details in enzymes.items():
        site = details["site"]
        cut_type = details["cut_type"]
        positions = []

        # Find all positions of the recognition site in the DNA sequence
        start = 0
        while start < len(dna_sequence):
            pos = dna_sequence.find(site, start)
            if pos == -1:
                break
            positions.append(pos + 1)  # Use 1-based index
            start = pos + 1

        if positions:
            results.append({
                "enzyme": enzyme,
                "site": site,
                "positions": positions,
                "cut_type": cut_type
            })

    return results


def write_log_file(results, filename="log.txt"):
    with open(filename, "w") as log_file:
        log_file.write(f"\n{datetime.datetime.now()}\n")
        log_file.write("Restriction Enzyme Analysis Log\n")
        log_file.write(f"Input DNA Sequence: {dna_sequence}\n")
        log_file.write("================================\n\n")


        if not results:
            log_file.write(f"{datetime.datetime.now()} - No restriction sites found in the given DNA sequence.\n")
        else:
            for result in results:
                log_file.write(f"\nEnzyme: {result['enzyme']}\n")
                log_file.write(f"Recognition Site: {result['site']}\n")
                log_file.write(f"Positions: {', '.join(map(str, result['positions']))}\n")
                log_file.write(f"Cut Type: {result['cut_type']}\n")
                log_file.write("--------------------------------\n")


def display_results(results):
    print(f"\n{datetime.datetime.now()}")
    print("Restriction Enzyme Analysis Results")
    print(f"Input DNA Sequence: {dna_sequence}")
    print("================================\n")

    if not results:
        print(f"{datetime.datetime.now()} - No restriction sites found in the given DNA sequence.")
    else:
        for result in results:
            print(f"\nEnzyme: {result['enzyme']}")
            print(f"Recognition Site: {result['site']}")
            print(f"Positions: {', '.join(map(str, result['positions']))}")
            print(f"Cut Type: {result['cut_type']}")
            print("--------------------------------")


# Main program
if __name__ == "__main__":
    # Example input
    dna_sequence = input("Enter the DNA sequence: ")

    # Find restriction sites
    results = find_restriction_sites(dna_sequence)

    # Display results
    display_results(results)

    # Write to log file
    write_log_file(results)

    print("\nAnalysis complete. Results saved to log.txt.")