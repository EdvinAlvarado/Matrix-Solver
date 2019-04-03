#include <iostream>
#include "terminal_command.h"
#include <string>
#include <vector>
#include <cmath> // sqrt

using namespace std;
vector<double> m; // matrix
int n; // dimension length of the main matrix
void command_lookup(char arg) { //Maybe change char to string
	if (arg == "exit") {
		shell_exit();
	}
	else if (arg.find("matrix") == 0) {
		string data_file_name = arg.substr(6,arg.size()-7);
		m = shell_matrix(data_file_name);
		n = (-1+sqrt(1+4*m.size()))/2;
		shell_view(m);
		MatrixChecker(m);
	}
	else if (arg == "view") {
		shell_view(m);
		MatrixChecker(m);
	}
	else if (arg.find("rowop") == 0) {
		// add rowop function and and arg extractor
		shell_view(m);
		MatrixChecker(m);

	}
	else if (arg.find("rowmult") == 0) {
		// add rowop function and and arg extractor
		shell_view(m);
		MatrixChecker(m);
	}
	else {
		cout << "Unknown Command" << endl;
	}
	cout << "\n";
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