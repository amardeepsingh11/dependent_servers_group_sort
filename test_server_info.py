from dependent_servers_group_sort import ServersInfo


# Program execution starting point
# create an object that contains servers information
s = ServersInfo()

# read the CSV and put values into the servers information object created above
#if s.readCSV('C:\\Users\\amardeep.singh\\Documents\\Automated_Patching\\ServerDependencyList\\samplePatchMetadata-Complex.csv') != True:
#csvFile = 'sample_inputs\\samplePatchMetadata-Simple.csv'
#csvFile = 'sample_inputs\\samplePatchMetadata-Complex.csv'
csvFile = 'sample_inputs\\samplePatchMetadata-Complex-MultipleGroups.csv'
#csvFile = 'sample_inputs\\samplePatchMetadata-Cyclic-1group.csv'
#csvFile = 'sample_inputs\\samplePatchMetadata-Cyclic-1group_in_Multiple_Groups.csv'

flag = s.readCSV(csvFile)

if not flag:
    print('read CSV fail')
    exit()

# do some initial validations on the data received from CSV
flag = s.validateServers()
if not flag:
    print('validateServers fail')
    exit()

# Group the serves using BFS and Order using topological sort
flag = s.groupServerBFSandTopoSort()
if not flag:
    print('groupServerBFSandTopoSort fail')
    exit()

# writes to JSON file
s.writeToJson(csvFile + '.json')

# print values ServerName, Group and Order to the console
s.printServer()