import pandas
from tqdm import tqdm
from rcv import PreferenceSchedule, FractionalSTV
from glob import glob
from pathlib import Path


def generate_results(groups):
    for precinct, group in groups.items():
        if len(set(group.values.ravel())) <= 3:
            continue
        winners = run_stv(group)
        yield [precinct] + list(winners)


def run_stv(dataframe):
    assert len(dataframe.columns) == 3
    schedule = PreferenceSchedule.from_dataframe(dataframe)
    stv = FractionalSTV(schedule, seats=3)
    return stv.elect()


def run_for_file(filename, output_file):
    df = pandas.read_csv(filename)
    choice_columns = list(df.columns)[1:4]

    groups = {
        precinct: df[choice_columns].loc[group]
        for precinct, group in df.groupby(df.Precinct).groups.items()
    }
    results = pandas.DataFrame(
        tqdm(generate_results(groups), total=len(groups), desc="Precincts"),
        columns=["Precinct"] + [f"Winner_{i}" for i in [1, 2, 3]],
    )
    results.set_index("Precinct").to_csv(output_file)
    return results


def main(folder):
    path = Path(folder)
    for filename in tqdm(glob(str(path / "*.csv")), desc="Elections"):
        output_folder = Path("./outcomes") / path.stem
        output_file = str(output_folder / f"{Path(filename).stem}-outcomes.csv")
        run_for_file(filename, output_file)


if __name__ == "__main__":
    main("minneapolis")
