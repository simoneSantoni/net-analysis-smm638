# %%
# load modules
import tabula


# %%
# convert PDF into CSV file
tabula.convert_into("paper.pdf", "output.csv", output_format="csv", pages="10")

# %%
# Read remote pdf into list of DataFrame
dfs2 = tabula.read_pdf(
    "https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf"
)

# %%
