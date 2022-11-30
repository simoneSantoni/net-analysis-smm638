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
# -- wrap the data together
data <- sienaDataCreate(friendship, quit, gender)
# %%

# %% get a report for the loaded siena 'data' objects
print01Report(data, modelname = "null_model")
# %%

# %% create an initial siena 'effects' object
effs <- getEffects(data)
# %%


# ----------------------------------------------------------------------------
# Create a null model containing elementary effects only
# ----------------------------------------------------------------------------

# %% create and estimate a model
alg <- sienaAlgorithmCreate(useStdInits = TRUE, projname = "quit_fr")
null_model <- siena07(
        alg,
        data = data,
        effects = effs,
        returnDeps = TRUE
)
null_model
# %%

# %% assess the model GOF
# -- are we reproducing the observed indegree distribution of the network?
gof <- sienaGOF(
        null_model,
        IndegreeDistribution,
        verbose = TRUE,
        join = TRUE,
        varName = "friendship"
)
plot(gof)
# --+ are we reproducing the observed outdegree distribution of the network?
gof <- sienaGOF(
        null_model,
        OutdegreeDistribution,
        verbose = TRUE,
        join = TRUE,
        varName = "friendship"
)
plot(gof)
# %%

# ----------------------------------------------------------------------------
# Expand on the null model by adding a network rule
# ----------------------------------------------------------------------------

# %% add a triadic closure effect
effs <- includeEffects(effs, gwespFF)
model_1 <- siena07(
        alg,
        data = data,
        effects = effs,
        returnDeps = TRUE,
        verbose = TRUE
)
model_1
# %%

# ----------------------------------------------------------------------------
# Expand on model_1 by adding a social selection rule
# ----------------------------------------------------------------------------

# %% gender and quit similarity influence network change
effs <- includeEffects(effs, egoX, altX, simX, interaction1 = "gender")
effs <- includeEffects(effs, egoX, altX, simX, interaction1 = "quit")
model_2 <- siena07(
        alg,
        data = data,
        effects = effs,
        returnDeps = TRUE,
        verbose = TRUE
)
model_2
# %%

# ----------------------------------------------------------------------------
# Expand on model_2 by adding a social influence rule
# ----------------------------------------------------------------------------

# %% alters' quit intentions influence network change
effs <- includeEffects(effs, name = "quit", avSim, interaction1 = "friendship")
model_3 <- siena07(
        alg,
        data = data,
        effects = effs,
        returnDeps = TRUE,
        verbose = TRUE
)
model_3
