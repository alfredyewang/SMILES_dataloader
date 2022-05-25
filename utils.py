


def read_delimited_file(file_path, ignore_invalid=True, num=-1):
    """
    Reads a file with SMILES strings in the first column.
    :param randomize: Standardizes smiles.
    :param standardize: Randomizes smiles.
    :param file_path: Path to a SMILES file.
    :param ignore_invalid: Ignores invalid lines (empty lines)
    :param num: Parse up to num rows.
    :return: An iterator with the rows.
    """
    actions = []
    with open(file_path, "r") as csv_file:
        for i, row in enumerate(csv_file):
            if i == num:
                break
            splitted_row = row.rstrip().replace(",", " ").replace("\t", " ").split()
            smiles = splitted_row[0]
            for action in actions:
                if smiles:
                    smiles = action(smiles)
            if smiles:
                yield smiles
            elif not ignore_invalid:
                yield None