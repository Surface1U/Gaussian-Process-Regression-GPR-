import csv
import json
import os, glob

def add_day(yyyy,mm,dd):
    dd+=1
    if dd > 27:
        if yyyy % 4 == 0:
            feb = 29
        else:
            feb = 28
        if (dd == feb + 1 and mm == 2):
            mm = 3
            dd = 1
        elif dd == 31 and ((mm % 2 == 1 and mm > 8) or (mm % 2 == 0 and mm < 8)):
            mm +=1
            dd = 1
        elif dd == 32:
            mm += 1
            dd = 1
        if mm == 13:
            yyyy +=1
            mm = 1
    return yyyy,mm,dd

def to_dir(yyyy,mm,dd):
    if dd<10:
        dds = "0" + str(dd)
    else:
        dds = str(dd)
    if mm<10:
        mms = "0" + str(mm)
    else:
        mms = str(mm)    
    return (str(yyyy)+"-"+str(mms)+"-"+str(dds))


def func_keys(data1):
    keys = data1.keys()
    for key in keys:
        try:
            try:
                #print("data: " + str(data1))
                small_data = data1[key]
                
                small_data =  json.dumps(small_data)
                
                small_data = json.loads(small_data)
                
                func_keys(small_data)
                
            except:
                values = list(find_values(data, key))
                small_data = json.dumps(values)
                small_data = small_data[1:-1]
                
                small_data = json.loads(small_data)
                
                func_keys(small_data)
        except:
            global listik, l1
            
            for i in range(len(listik)):
                if listik[i] == str(key) or str(key) == listik[i][0].lower() + listik[i][1:]:

                    if str(key) == "Latency":
                        print ("Latency = " + data1[key])
                    l1[i] = str(data1[key])
                    break
               
            print("Key: " + str(key))
            print("Value: " + str(data1[key]))
            print()
                          
            
def find_values(data, key):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                yield v
            elif isinstance(v, (dict, list)):
                yield from find_values(v, key)
    elif isinstance(data, list):
        for item in data:
            yield from find_values(item, key)              



path1 = 'D:/Leto/Data'
dd = 1
mm = 12
yyyy = 2022
listik = ['Innodb_adaptive_flushing_lwm', 'Innodb_adaptive_hash_index', 'Innodb_adaptive_max_sleep_delay', 'Innodb_buffer_pool_instances', 'Innodb_buffer_pool_size', 'Innodb_change_buffering', 'Innodb_io_capacity', 'Innodb_log_file_size', 
           'Innodb_max_dirty_pages_pct', 'Innodb_max_dirty_pages_pct_lwm', 'Innodb_sync_array_size', 'Innodb_thread_concurrency', 'Max_heap_table_size', 'Thread_cache_size', 'Tmp_table_size', 
           '|||', 
           'Binlog_cache_size', 'Binlog_max_flush_queue_time', 'Binlog_stmt_cache_size', 'Eq_range_index_dive_limit', 'Host_cache_size', 'Innodb_adaptive_flushing', 'Innodb_autoextend_increment', 'Innodb_buffer_pool_dump_now', 
           'Innodb_buffer_pool_load_at_startup', 'Innodb_buffer_pool_load_now', 'Innodb_change_buffer_max_size', 'Innodb_commit_concurrency', 'Innodb_compression_failure_threshold_pct', 'Innodb_compression_level', 'Innodb_compression_pad_pct_max', 
           'Innodb_concurrency_tickets', 'Innodb_flush_log_at_timeout', 'Innodb_flush_neighbors', 'Innodb_flushing_avg_loops', 'Innodb_ft_cache_size', 'Innodb_ft_result_cache_limit', 'Innodb_ft_sort_pll_degree', 'Innodb_io_capacity_max', 
           'Innodb_lock_wait_timeout', 'Innodb_log_buffer_size', 'Innodb_lru_scan_depth', 'Innodb_max_purge_lag', 'Innodb_max_purge_lag_delay', 'Innodb_old_blocks_pct', 'Innodb_old_blocks_time', 'Innodb_online_alter_log_max_size', 'Innodb_page_size', 
           'Innodb_purge_batch_size', 'Innodb_purge_threads', 'Innodb_random_read_ahead', 'Innodb_read_ahead_threshold', 'Innodb_read_io_threads', 'Innodb_replication_delay', 'Innodb_rollback_segments', 'Innodb_sort_buffer_size', 'Innodb_spin_wait_delay', 
           'Innodb_sync_spin_loops', 'Innodb_thread_sleep_delay', 'Innodb_use_native_aio', 'Innodb_write_io_threads', 'Join_buffer_size', 'Lock_wait_timeout', 'Max_binlog_cache_size', 'Max_binlog_size', 'Max_binlog_stmt_cache_size', 'Max_delayed_threads', 
           'Max_insert_delayed_threads', 'Max_join_size', 'Max_length_for_sort_data', 'Max_seeks_for_key', 'Max_sort_length', 'Max_sp_recursion_depth', 'Max_tmp_tables', 'Max_write_lock_count', 'Metadata_locks_cache_size', 'Optimizer_prune_level', 
           'Optimizer_search_depth', 'Preload_buffer_size', 'Query_alloc_block_size', 'Query_cache_limit', 'Query_cache_min_res_unit', 'Query_cache_size', 'Query_cache_type', 'Query_cache_wlock_invalidate', 'Query_prealloc_size', 'Range_alloc_block_size', 
           'Read_buffer_size', 'Read_rnd_buffer_size', 'Slave_checkpoint_group', 'Slave_checkpoint_period', 'Slave_parallel_workers', 'Slave_pending_jobs_size_max', 'Sort_buffer_size', 'Stored_program_cache', 'Table_definition_cache', 'Table_open_cache', 
           'Table_open_cache_instances', 'Thread_stack', 'Timed_mutexes', 'Transaction_alloc_block_size', 'Transaction_prealloc_size', 
           '|||', 
           'Binlog_group_commit_sync_delay', 'Binlog_group_commit_sync_no_delay_count', 'Innodb_adaptive_hash_index_parts', 'Innodb_buffer_pool_chunk_size', 'Innodb_buffer_pool_dump_pct', 'Innodb_disable_sort_file_cache', 'Innodb_flush_sync', 
           'Innodb_ft_total_cache_size', 'Innodb_log_write_ahead_size', 'Innodb_max_undo_log_size', 'Innodb_page_cleaners', 'Innodb_purge_rseg_truncate_frequency', 'Range_optimizer_max_mem_size', 'Rpl_stop_slave_timeout', 'Slave_allow_batching', 
           'Slave_parallel_type', 
           '|||', 
           'Innodb_dedicated_server', 'Innodb_doublewrite_batch_size', 'Innodb_doublewrite_files', 'Innodb_doublewrite_pages', 'Innodb_log_files_in_group', 'Innodb_log_spin_cpu_abs_lwm', 'Innodb_log_spin_cpu_pct_hwm', 
           'Innodb_log_wait_for_flush_spin_hwm', 'Max_relay_log_size', 'Open_files_limit', 'Parser_max_mem_size', 'Relay_log_space_limit', 'Rpl_read_size', 'Stored_program_definition_cache', 'Tablespace_definition_cache', 'Temptable_max_ram', 
           '|||', 
           'version_comment', 'version', 'Latency']

    
li1 = [""] * (len(listik))
for i in range (len(listik)):
    li1[i] = listik[i]
li1.append('filename')

with open("data1.csv", mode="w", encoding='utf-8', newline='') as w_file:
    file_writer = csv.writer(w_file, delimiter=",")
    file_writer.writerow(li1)
    
    while True:
        
            path2 = to_dir(yyyy, mm, dd)
            
            path = os.path.join(path1, path2)
            
            path = "D:/Leto/Data/2023-01-04/5df6a6f5-cf74-4c91-a5b3-204452dc60db.json"
            for filename in glob.glob(path):
            #for filename in glob.glob(os.path.join(path, '*.json')):
                with open(filename, 'r') as f:
                    print(filename)
                    json_str = f.read()
                    data = json.loads(json_str)
                    l1=[' '] * len(listik)
                    l = []                
                    keys = data.keys()
                    func_keys(data)
                    
                    for i in range (len(l1)):
                        if listik[i] != "|||":
                            l.append(l1[i])
                        else:
                            l.append("|||")
                    l.append(filename)
                    
                    if l1[len(listik)-1] != " ":
                        
                        print("ADDED")
                        file_writer.writerow(l)
                    
            yyyy, mm, dd = add_day(yyyy, mm, dd)
            
print("Done") 
