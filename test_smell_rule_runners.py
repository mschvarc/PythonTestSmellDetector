import test_smells.test_method_smells as test_method_smells
import test_smells.test_case_smells as test_case_smells
import test_smells.project_smells as project_smells

def project_rule_runner(python_files):
    """Run rules that need the entire python project to detect a smell"""
    
    project_smell_list = list()
    project_smell_list.append(project_smells.LazyTest())
    project_smell_list.append(project_smells.EagerTest())
    
    output = list()
    
    for smell in project_smell_list:
    
        result = smell.test_for_smell(python_files)
        
        if result is not None:
            output = output + result
    
    return output
    
def test_case_rule_runner(test_case_ast_pair):
    """Run rules that only need a test case to detect a smell
    
    Accepts a pair with a test case AST and their file of origin, and runs each 
    of the defined test case rules on the AST."""
    
    test_case_smell_list = list()
    test_case_smell_list.append(test_case_smells.GeneralFixture())
    test_case_smell_list.append(test_case_smells.ConstructorInitialization())
    test_case_smell_list.append(test_case_smells.DefaultTest())
    
    output = list()
    
    for smell in test_case_smell_list:
    
        result = smell.test_for_smell(test_case_ast_pair[0])
        
        if result is not None:
        
            output.append((result,test_case_ast_pair[1]))
    
    return output
    
def test_method_rule_runner(test_method_ast_pair):
    """Run rules that need the entire test method to detect a smell"""
    
    #all of the smells run in the test_method_rule_runner get added to the 
    #method_smell_list
    method_smell_list = list()
    method_smell_list.append(test_method_smells.MagicNumberTest())
    method_smell_list.append(test_method_smells.SensitiveEquality())
    method_smell_list.append(test_method_smells.ConditionalTestLogic())
    method_smell_list.append(test_method_smells.DuplicateAssertTest())
    method_smell_list.append(test_method_smells.EmptyTest())
    method_smell_list.append(test_method_smells.ExceptionCatchingAndThrowing())
    method_smell_list.append(test_method_smells.SkippedTest())
    method_smell_list.append(test_method_smells.RedundantPrint())
    method_smell_list.append(test_method_smells.RedundantAssert())
    method_smell_list.append(test_method_smells.SleepyTest())
    method_smell_list.append(test_method_smells.MysteryGuest())
    method_smell_list.append(test_method_smells.UnknownTest())
    
    output = list()
    
    for smell in method_smell_list:
    
        result = smell.test_for_smell(test_method_ast_pair[0])
        
        if result is not None:
        
            result_pair = (result, test_method_ast_pair[0].name, test_method_ast_pair[1])
            
            output.append(result_pair)
    
    return output
    