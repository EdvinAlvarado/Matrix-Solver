#include <iostream>
#include "terminal_command.h"
#include <string>
#include <vector>

using namespace std;
vector<double> m;
int rowsize;
int colsize;
void command_lookup(char arg) { //Maybe change char to string
	if (arg == "exit") {
		shell_exit()
	}
	elif (arg.find("matrix") == 0) {
		string data_file_name = arg.substr(6,arg.size()-7);
		m = shell_matrix(data_file_name);
		x2+x-s=0
	}
}


int main() {
	int counter = 1;
	string args;
	while (true) {
		cout << "[" << counter << "] ";
		cin >> args;
		cout << "\n";
		counter += 1;
		if (args == "") {
			cout << endl;
			continue
		}
		else {
			command_lookup(args);
		}
	}
}