def calculate_storage(file_count:int,file_size_mb: float)->float:
   return file_count*file_size_mb
def calculate_average(total_size_mb:float,file_count:int)->float:
   return total_size_mb / file_count
def split_logs(log_files:int, archive_size:int)->tuple[int,int]:
   full_archives=log_files // archive_size
   remaining_logs = log_files%archive_size
   return full_archives, remaining_logs
def calculate_code_combinations(characters: int,code_length:int)->int:
   return characters ** code_length
def main()-> None:
    file_count = 25
    file_size_mb = 8.0
    storage_limit_mb = 250.0
    total_size_mb = calculate_storage(file_count,file_size_mb)
    remaining_storage_mb = storage_limit_mb - total_size_mb
    average_size_mb = calculate_average(total_size_mb, file_count)
    print("LOG STORAGE")
    print(f"total storage used:{total_size_mb}MB")
    print(f"storage_remaining:{remaining_storage_mb}MB")
    print(f"average file size:{average_size_mb}MB")

    log_files=137
    archive_size =12
    full_archives, remaining_files = split_logs(log_files,archive_size)

    print("\nLOG ARCHIVES")
    print(f"Full archives:{full_archives}")
    print(f"Files remaining: {remaining_files}")

    characters = 10 
    code_length = 4
    possible_codes = calculate_code_combinations(characters,code_length)

    print("\nCODE COMBINATIONS")
    print(f"Possible codes:{possible_codes}")

if __name__=="__main__":
    main()
