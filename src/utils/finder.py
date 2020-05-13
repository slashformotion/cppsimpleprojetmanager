import pathlib as pl

def extensive_find_main_file(path):
    """
    find cpp files and return extensives information

    Args:
        path (pathlib.Path): path to a folder

    Returns:
        tuple(int, list(pathlib.Path)): number of main files found, list of the main files found
    """
    return len(find_main_file(path)), find_main_file(path)

def find_main_file(path):
    """
    find_main_file find .cpp files with an "int main(args)" function declaration        
    
    Args:
        path (pathlib.Path): path to a folder
    
    Returns:
        list(path like objects)
    """
    file_list = []
    for cpp in find_files(path, "cpp"):
        cpp = pl.Path(cpp)
        with cpp.open('r') as flux:
            cpp_content = flux.read()
            if "int main(" in cpp_content:
                file_list.append(cpp)
    return file_list

def find_cpp(path):
    """
    find <.cpp> files in path 

    Args:
        path (pathlib.Path): folder to search

    Returns:
        list(pathlib.Path): path to the <.cpp> files in the directory
    """
    return find_files(path, "cpp")

def find_headers(path):
    """
    find_headers find the files ending with ".hpp" in the path given as an argment
    
    Args:
        path (pathlib.Path): directory where the function search for .hpp files
    
    Returns:
        list(pathlib.path): list of the headers found
    """
    file_list = []
    for cpp in find_files(path, "hpp"):
        file_list.append(cpp)
    return file_list


def find_files(path, ext):
    """
    find_files : return files with <.ext> at the given path
    
    Args:
        path (pathlib.Path): where to search files  
        ext (str): extension of the files to retreive
    
    Returns:
        list(pathlib.Path): list of the path of the files searched
    """
    assert isinstance(ext, str)
    assert path.is_dir()
    file_list = []
    for cpp in sorted(path.glob(f"*.{ext}")):
        file_list.append(pl.Path(cpp)) 
    return file_list

    


if __name__ == "__main__":
    # test __func__ find_main_file()
    print(find_cpp(pl.Path("/home/slash/Documents/Programmation/projets/cppsimpleprojetmanager/test/lib")))
    
