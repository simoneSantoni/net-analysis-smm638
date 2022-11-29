#----------------------------------------------------------------------------
# Load R modules
#----------------------------------------------------------------------------
# %% load module
library(RSiena)
# %%

# %% set work directory
print(getwd())
setwd("beamers/networkMechanisms/partIII/saom")
# %%

# %% load data
friend1 <- as.matrix(read.table("MH-friend1.dat"))
friend2 <- as.matrix(read.table("MH-friend2.dat"))
friend3 <- as.matrix(read.table("MH-friend3.dat"))
quit <- as.matrix(read.table("attribute-quit.dat"))
gender <- as.matrix(read.table("attribute-gender.dat"))
# %%

# %% create siena 'data' objects
# -- network
friendship <- sienaDependent(array(c(friend1, friend2, friend3), dim = c(32, 32, 3)))
# -- behavior
quit <- sienaDependent(quit, type = "behavior")
# -- attributes
gender <- coCovar(gender[, 1])
# -- wrap the data togethe
data <- sienaDataCreate(friendship, quit, gender)
# %%

# %% get a report for the loaded siena 'data' objects
print01Report(data, modelname = "null_model")
# %%

# %% create an initial siena 'effects' object
effs <- getEffects(data)
# %%


# %% create and estimate a model
alg <- sienaAlgorithmCreate(useStdInits = TRUE, projname = "quit_fr")
null_model.results <- siena07(
        alg,
        data = data,
        effects = effs,
	returnDeps = TRUE
)
null_model.results
# %%

# %% assess the model GOF
# -- are we reproducing the observed indegree distribution of the network?
gof <- sienaGOF(
        null_model.results,
        IndegreeDistribution,
        verbose = TRUE,
        join = TRUE,
        varName = "friendship"
)
plot(gof)
# --+ are we reproducing the observed outdegree distribution of the network?
gof <- sienaGOF(
        null_model.results,
        OutdegreeDistribution,
        verbose = TRUE,
        join = TRUE,
        varName = "friendship"
)
plot(gof)

# %% add a new effect network effect
MyEff <- includeEffects(MyEff, gwespFF)
Model1.results <- siena07(
        Model1,
        data = MyData,
        effects = MyEff,
        returnDeps = TRUE,
        verbose = TRUE
)
Model1.results

MyEff <- includeEffects(MyEff, egoX, altX, simX, interaction1 = "gender")
MyEff <- includeEffects(MyEff, egoX, altX, simX, interaction1 = "quit")
Model1.results <- siena07(
        Model1,
        data = MyData,
        effects = MyEff,
        returnDeps = TRUE,
        verbose = TRUE
)
Model1.results

# ----------------------------------------------------------------------------
# Modeling social influence
# ----------------------------------------------------------------------------

MyEff <- includeEffects(MyEff, name = "quit", avSim, interaction1 = "friendship")
soc_influence <- siena07(Model1, data = MyData, effects = MyEff)
soc_influence.results
