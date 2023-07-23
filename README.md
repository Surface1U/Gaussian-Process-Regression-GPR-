# Gaussian Process Regression (GPR)
________________________________________________________________

# What have we done?

gpr_model.py directly extracts data from csv files and reproduces the received data. The learning results are saved in csv files, which are stored in the csvs folder (
## one.csv - for MySQL versions 5.6 and higher, 
## two.csv - Knobs Tuned in MySQL 5.6 and higher, 
## three.csv - Knobs Tuned in MySQL 5.7 and Higher, 
## thre.csv - Knobs Tuned in MySQL 8
).
The optimal values for the kernel hyperparameters are shown below. For parameters from certain MySQL versions and optimal values FOR ALL PARAMETERS FROM JSON files.




### test1

# for MySQL versions 5.6 and higher

Score on test data: 0.7641731141736772


# Knobs Tuned in MySQL 5.6 and higher
Score on test data: -6.240741416508203e+28
prediction values

# Knobs Tuned in MySQL 5.7 and Higher
Score on test data: 0.6666666635046372


# Knobs Tuned in MySQL 8
Score on test data: 0.9999111331137519

______________________________________________________________________________

### test 2
# for MySQL versions 5.6 and higher
Score on test data: 0.9999874571976871

# Knobs Tuned in MySQL 5.6 and higher
Score on test data: -668552508.0733334

# Knobs Tuned in MySQL 5.7 and Higher
Score on test data: 0.6666666657571554

# Knobs Tuned in MySQL 8
Score on test data: 0.9998903158165987
__________________________________________________________________

### test 3

# for MySQL versions 5.6 and higher
Score on test data: 0.9982711147289386


# Knobs Tuned in MySQL 5.6 and higher
Score on test data: 0.5317091501568023


# Knobs Tuned in MySQL 5.7 and Higher
Score on test data: 0.6666666663215584


# Knobs Tuned in MySQL 8

Score on test data: 0.9999874216621232



### test 4

# for MySQL versions 5.6 and higher
Score on test data: 0.9509018764837927


# Knobs Tuned in MySQL 5.6 and higher
Score on test data: -5.20061784709017e+27


# Knobs Tuned in MySQL 5.7 and Higher
Score on test data: 0.6666666664023441



# Knobs Tuned in MySQL 8
Score on test data: 0.9999865550089736



### test 5

# for MySQL versions 5.6 and higher
Score on test data: 0.9999871588652225


# Knobs Tuned in MySQL 5.6 and higher
Score on test data: 0.6169098320959082


# Knobs Tuned in MySQL 5.7 and Higher

Score on test data: 0.6666666665365281


# Knobs Tuned in MySQL 8
Score on test data: 0.9999944101099251


### test 6

# for MySQL versions 5.6 and higher
Score on test data: 0.9498159229116723


# Knobs Tuned in MySQL 5.6 and higher
Score on test data: 0.6666666545203808


# Knobs Tuned in MySQL 5.7 and Higher
Score on test data: 0.6666666665672506

# Knobs Tuned in MySQL 8
Score on test data: 0.9333303134970667

# Knobs Tuned in MySQL 5.6 and higher

Optimal kernel hyperparameters:
Length Scale: 100000.00000000001
Negative Log Likelihood: 7.306630254159028e+40
Speed of convergence of parameter estimates: 1.0
Speed of convergence of predictions: 0.0

# for MySQL versions 5.6 and higher

Optimal kernel hyperparameters:
Length Scale: 100000.00000000001
Negative Log Likelihood: 2.9291278004543295e+19
Speed of convergence of parameter estimates: 1.0
Speed of convergence of predictions: 0.0

# Knobs Tuned in MySQL 5.7 and Higher

Optimal kernel hyperparameters:
Length Scale: 100000.00000000001
Negative Log Likelihood: 5.301198696982859e+18
Speed of convergence of parameter estimates: 1.0
Speed of convergence of predictions: 0.0


# Knobs Tuned in MySQL 8

Optimal kernel hyperparameters:
Length Scale: 100000.00000000001
Negative Log Likelihood: 1.4128745816341852e+39
Speed of convergence of parameter estimates: 1.0
Speed of convergence of predictions: 0.0


# data.csv 

Optimal kernel hyperparameters:
Length Scale: 100000.00000000001
Negative Log Likelihood: 7.306630254159368e+40
Speed of convergence of parameter estimates: 1.0
Speed of convergence of predictions: 0.0
_______________________________________________________________
