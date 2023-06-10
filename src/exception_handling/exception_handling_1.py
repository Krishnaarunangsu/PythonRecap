import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    # print("OS error:", err)
    raise FileNotFoundError("No Such File Exist") from err
except ValueError:
    print("Could not convert data to an integer.")
#except Exception as err:
    #print(f"Unexpected {err=}, {type(err)=}")
    #raise
finally:
    print("Jagannath")