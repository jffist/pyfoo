import pkg_resources
import os

def main_easy_but_not_recommened():
    sql_dir = os.path.join(os.path.dirname(__file__), 'sql')
    for query_name in os.listdir(sql_dir):
        print('--- start:', query_name)
        print(open(os.path.join(sql_dir, query_name)).read())
        print('--- end:', query_name)
        print()
        
# based on https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
def main():
    # Could be any dot-separated package/module name or a "Requirement"
    resource_package = __name__
    for query_name in pkg_resources.resource_listdir(resource_package,'sql'):
        print('--- start:',query_name)
        resource_path = '/'.join(('sql', query_name))  # Do not use os.path.join()
        query = pkg_resources.resource_string(resource_package, resource_path)
        print(query)
        print('--- end:',query_name)
        print()


if __name__ == '__main__':
    main()
