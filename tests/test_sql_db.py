def full_time_parse_and_db():
    start_time = time.time()
    temp_data = time_test_parse()
    update_peers_sessions(temp_data)
    print("updated db on ", time.time() - start_time)
