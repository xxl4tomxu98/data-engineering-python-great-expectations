import great_expectations as ge
print(ge.__version__)
# add great_expectations/plugins to path
import sys, os
import datetime

project_dir = "./ge_context/choose_your_adventure"
os.makedirs(project_dir)
context = ge.data_context.DataContext.create(project_dir)

pandas = context.add_datasource(
    "pandas",
    class_name="PandasDatasource",
)

context = ge.data_context.DataContext(os.path.join(project_dir, "great_expectations"))
batch_kwargs = context.build_batch_kwargs("pandas", "manual", "titanic")
# What expectation suite shall we use? Why, the "adventure" suite of course:
expectation_suite_name = "adventure"
# Demo Mode? Uncomment the below first to use an empty validation suite
# suite = context.create_expectation_suite(expectation_suite_name)