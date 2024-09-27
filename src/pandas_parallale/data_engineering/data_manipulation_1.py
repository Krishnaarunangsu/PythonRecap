from pyspark.sql.functions import lit
from src.pandas_parallale.spark_initialization.spark_initialization import SparkInitialization

class DataManipulation:
    """

    """
    def __init__(self):
        """

        """
        SparkInitialization.__init__(self)
        self.spark_initialization=SparkInitialization()
        self.spark=self.spark_initialization.get_spark_object()
        self.dataframe=None
        self.dataframe_filtered=None
        self.dataframe_ordered=None
        self.dataframe_aggregate = None
        self.dataframe_updated = None

    def create_dataframe(self,data, columns):
        """

        Returns:

        """
        self.dataframe=self.spark.createDataFrame(data, schema=columns)
        print(f'The Dataframe is:')
        self.dataframe.show()

    def filter_by_age(self,age:int):
        """

        Args:
            age:

        Returns:

        """
        self.dataframe_filtered=self.dataframe.filter(self.dataframe["Age"] > age)
        print(f'The filtered Dataframe:')
        self.dataframe_filtered.show()
        #self.spark.stop()

    def show_selected_columns(self, *cols):
        """

        Args:
            *columns:

        Returns:

        """
        for column in cols:
            print(column)
        # s=["Name", "Age"]
        # self.dataframe.select(*cols).show()
        self.dataframe.select(*cols).show()

    def sort_data_column(self, column):
        """

        Returns:

        """
        print(f'Sort Column:{column}')
        self.dataframe_ordered=self.dataframe.orderBy(self.dataframe[column])
        self.dataframe_ordered.show()

    def group_aggregate(self, group_column, aggregate_column,aggregate_function):
        """

        Args:
            group_column:
            aggregate_column:
            aggregate_function:

        Returns:

        """
        print(f'Group Column:{group_column}')
        print(f'Aggregate Column:{aggregate_column}')
        self.dataframe_aggregate=self.dataframe.groupBy(group_column).agg({aggregate_column:aggregate_function})
        self.dataframe_aggregate.show()

    def add_new_column(self, column_name, column_value:str):
        """

        Args:
            column_name:
            column_value:

        Returns:

        """
        self.dataframe_updated = self.dataframe.withColumn("Nationality", lit("Indian"))
        # self.dataframe_updated=self.dataframe.withColumn(column_name, column_name)
        self.dataframe_updated.show()





if __name__=="__main__":
    data_manipulation=DataManipulation()
    data=[('Alice','M', 25),('Bob','M', 30), ('Charlie','F', 35)]
    columns=["Name","Gender","Age"]
    data_manipulation.create_dataframe(data,columns)
    filter_age=30
    data_manipulation.filter_by_age(filter_age)

    # array = []
    # for i in range(4):
    #     array.append(input("Enter string"))
    #
    #array = [input("Enter string: ") for i in range(2)]
    #print(array)


    # n = int(input("Enter the number of names in list for input:"))
    # print(n)
    # print(type(n))
    # a=[]
    # a = [input() for i in range(n)]

    #data_manipulation.show_selected_columns(*array)
    data_manipulation.sort_data_column("Age")
    data_manipulation.group_aggregate("Gender", "Age","sum")
    data_manipulation.add_new_column("Nationality", "Indian")