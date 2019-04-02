#include <iostream>
#include "terminal_command.h"
#include <string>

using namespace std;
void command_lookup(char arg) {
	if (arg == "exit") {
		shell_exit()
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