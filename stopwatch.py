import time

def main():
    start_time = time.time()
    input("Press ENTER to stop timer...")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()