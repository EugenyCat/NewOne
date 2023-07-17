"""Open for WRITE"""
f = open('files/results.csv', 'w')

f.write('Write first line\n')
f.write('Write second line\n')


"""Old Data are deleted"""
my_friend_results = open('files/results.csv', 'w')
my_friend_results.write('Write something else')

f.close()
my_friend_results.close()


"""Best practice"""
with open('files/results.csv', 'w') as f:
    f.write('Write first line\n')
    f.write('Write second line\n')

    """It doesn't change file"""
    my_friend_results = open('files/results.csv', 'w')
    my_friend_results.write('Write something else')
    my_friend_results.close()



"""Parallelize Read and Write"""
with open('files/visit_log.csv', 'r') as f:
    with open('files/visits_context.csv', 'w') as f2write:
        for line in f:
            if 'context' in line:
                f2write.write(line)



