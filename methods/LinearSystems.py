############################################### functions ##############################################################
# this function aims to return the correct position of the passed equation to put it in the list,checks if an error has occurred
def find_order_in_matrix(eq):
    eq_abs = list(map(abs, eq))  # a list carrying tha absolute values to use it in comparing
    for i in range(len(eq_abs)):
        if eq_abs[i] > sum(eq_abs) - eq_abs[i] - eq_abs[-1]:
            return i + 1
        elif eq_abs[i] == sum(eq_abs) - eq_abs[i] - eq_abs[-1]:
            if eq_abs.count(eq_abs[i]) == len(eq_abs) or eq_abs.count(eq_abs[i]) == len(eq_abs)-1:
                return -1  # we will check for -1 when using the function to handle those equations separately
            else:
                return i + 1
    raise Exception("INVALID INPUT : can't be solved using this numerical method")
    # if the equation can't be used in generating the diagonally dominant matrix , an error is raised !
# this functions returns the diagonally dominant matrix,checks if an error has occurred
def get_diagonally_dominant_matrix(num_EQs,list_of_inputs):
    # the function return a tuple, if tuple[1]==1 , the inputs is incorrect
    # declaring a lists and dictionaries
    dictionary_of_equations = {}
    list_of_equations = []
    list_of_equal_coff_equations = []  # the equations whose all coefficients are equal should be handled separately
    error_occurred=0
    #############################
    # generating the dictionary
    count =0
    for i in range(num_EQs):
        given_eq = []  # list should be cleaned after each iteration
        for j in range(num_EQs):
            coff = float(list_of_inputs[count]) # for the coffs. of the LHS
            count+=1
            given_eq.append(coff)
        coff = float(list_of_inputs[count]) # for the coff. of the RHS
        count += 1
        given_eq.append(coff)
        # the equation is read successfully
        #############################
        # checking if there is an equation with the same order then, raise an error
        if (find_order_in_matrix(given_eq) - 1) in dictionary_of_equations.keys():
            #raise Exception("INVALID INPUT : can't be solved by this numerical method!!!")
            error_occurred=1;
            # returning a tuble, check if tuple[1]==1 then the equation can't form the matrix
            return list_of_equations, error_occurred
        elif find_order_in_matrix(given_eq) == -2:
            error_occurred = 1;
            # returning a tuble, check if tuple[1]==1 then the equation can't form the matrix
            return list_of_equations, error_occurred
        else:
            if find_order_in_matrix(given_eq) == -1:
                list_of_equal_coff_equations.append(given_eq)  # to handle them separately
            else:
                dictionary_of_equations[find_order_in_matrix(given_eq) - 1] = given_eq
       # print(find_order_in_matrix(given_eq))

    #############################
    for i in range(num_EQs):
        # values of the keys should be continuous if not then the missed equation is in the "list_of_equal_coff_equations"
        if i not in dictionary_of_equations.keys():
            # checking that the "list_of_equal_coff_equations" has values
            if list_of_equal_coff_equations:
                dictionary_of_equations[i] = list_of_equal_coff_equations.pop(0)
    #############################
    # inserting the equations in the list with the correct order
    for i in range(num_EQs):
        list_of_equations.append(dictionary_of_equations[i])
    # returning a tuple, check if tuple[1]==1 then the equation can't form the matrix
    return list_of_equations, error_occurred
# this functions returns a tuple of 2-lists for the LHS and the RHS coffs
def get_tuple_of_LHS_and_RHS(n,diagonally_dominant_matrix): # tuple[0]->a | tuple[1]->b
    list_of_equations=diagonally_dominant_matrix
    a = []
    b = []
    for i in range(0, n):
        equation = []
        for j in range(0, n):
            equation.append(list_of_equations[i][j])
        a.append(equation)  # coffs. of the LHS
        b.append(list_of_equations[i][n])  # coffs. of the RHS
    return a,b
# this function checks if the equations are parallel
def are_equations_parallel(n,a,b): # n->num_EQs |a-> # coffs. of the LHS | b-> # coffs. of the RHS
    if n:  # if there are equations
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                parallel = True
                for k in range(0, n - 1):
                    if a[i][k + 1] != 0 and a[j][k + 1] != 0 and a[i][k] / a[i][k + 1] != a[j][k] / a[j][k + 1]:
                        parallel = False
                        break
                    elif (a[i][k + 1] != 0 and a[j][k + 1] == 0) or (a[i][k + 1] == 0 and a[j][k + 1] != 0):
                        parallel = False
                        break
                    elif a[i][k + 1] == 0 and a[j][k + 1] == 0:
                        if n == 2 or k + 1 == n - 1:
                            break
                        elif a[i][k + 2] != 0 and a[j][k + 2] != 0 and a[i][k] / a[i][k + 2] != a[j][k] / a[j][k + 2]:
                            parallel = False
                            break
    return parallel
# for calculations
def SOR(a, x, b,w):
    n = len(a)
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]
        for i in range(0, n):
            if (j != i):
                 d -= a[j][i] * x[i]
            # updating the value of our solution
        x[j] = (1-w) * x[j] + w * (d / a[j][j])
    # returningm , our updated solution
    return x
# this function solves the linear system and returns a tuple where tuple[0]->list with the answers | tuple[1]-> error_occurred
def solve_linear_systems(n,list_of_inputs,w,choice,num_iterations,error):
    # choice #1 -> oterations | choice #2 -> error
    # if the equations can't generate a diagonally dominant matrix then, error_occurred is 1, if parallel then,2
    empty_list=[]
    error_occurred=0
    tuple = get_diagonally_dominant_matrix(n, list_of_inputs)
    error_handling = tuple[1]
    if error_handling:
        error_occurred=1
        return empty_list,error_occurred
    list_of_equations = tuple[0]
#######################################
    tuple=get_tuple_of_LHS_and_RHS(n,list_of_equations)
    tuple = get_tuple_of_LHS_and_RHS(n, list_of_equations)
    a = tuple[0]
    b = tuple[1]
    if (are_equations_parallel(n,a,b)):
        error_occurred = 2
        return empty_list, error_occurred
#######################################
    roundTo = 6
    x = [1]  # intial guess
    x = n * x  # intial guess
    x_old = [1]
    x_old = n * x_old
    max_error_each_iteration = []
    all_errors_in_one_iteration = []
    list_of_iterations = []
    # loop run for m times depending on m the error value
    if choice == 1:
        for i in range(0, num_iterations):
            rounded_x = [round(num, roundTo) for num in x]
            list_of_iterations.append(rounded_x * 1)
            x = SOR(a, x, b, w)
            for k in range(0, n):
                if x[k] == 0:
                    continue
                all_errors_in_one_iteration.append((x[k] - x_old[k]) / x[k])

            if all_errors_in_one_iteration:
                abs_errors = list(map(abs, all_errors_in_one_iteration))
                max_error = max(abs_errors) * 1
                if max(all_errors_in_one_iteration) == max_error:
                    max_error = max_error * 1
                else:
                    max_error = -max_error * 1
            else:
                max_error = 0  # if the list of errors was empty then, the error equals zero

            all_errors_in_one_iteration = []
            max_error_each_iteration.append(max_error)
            x_old = x * 1

    elif choice == 2:
        status = True
        while True:
            status = False
            rounded_x = [round(num, roundTo) for num in x]
            list_of_iterations.append(rounded_x * 1)
            x = SOR(a, x, b, w)
            for k in range(0, n):
                if x[k] == 0:
                    continue
                all_errors_in_one_iteration.append((x[k] - x_old[k]) * 100 / x[k])
            abs_errors = list(map(abs, all_errors_in_one_iteration))
            if abs_errors !=[]:
                max_error = max(abs_errors) * 1
            else:
                max_error=0;
            if all_errors_in_one_iteration and max(all_errors_in_one_iteration) == max_error:
                max_error = max_error * 1
            else:
                max_error = -max_error * 1
            all_errors_in_one_iteration = []
            max_error_each_iteration.append(max_error)
            if abs(max_error) <= error:
                status = True
            x_old = x * 1
            if status == True:
                break

    rounded_x=[round(num,roundTo) for num in x]
    rounded_max_error_each_iteration=[round(num,roundTo) for num in max_error_each_iteration]
    return rounded_x, error_occurred, list_of_iterations, rounded_max_error_each_iteration, len(list_of_iterations)
