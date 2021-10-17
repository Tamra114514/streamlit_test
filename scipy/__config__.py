# This file is generated by C:\ci\scipy_1550684225850\work\setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

lapack_mkl_info={'libraries': ['mkl_rt'], 'library_dirs': ['C:/Users/tamu0/Anaconda3\\Library\\lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'C:/Users/tamu0/Anaconda3\\Library\\include']}
lapack_opt_info={'libraries': ['mkl_rt'], 'library_dirs': ['C:/Users/tamu0/Anaconda3\\Library\\lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'C:/Users/tamu0/Anaconda3\\Library\\include']}
blas_mkl_info={'libraries': ['mkl_rt'], 'library_dirs': ['C:/Users/tamu0/Anaconda3\\Library\\lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'C:/Users/tamu0/Anaconda3\\Library\\include']}
blas_opt_info={'libraries': ['mkl_rt'], 'library_dirs': ['C:/Users/tamu0/Anaconda3\\Library\\lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'C:/Users/tamu0/Anaconda3\\Library\\include']}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    