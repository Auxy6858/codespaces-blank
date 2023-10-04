#include <iostream>
int main(){
    bool REPEAT = true;
    std::string UserChoice;
    while(REPEAT == true) {

        std::cout << "Would you like to run the program? (y/n)\n";
        std::cin >> UserChoice;

        if(UserChoice == "y") {
            const float Pi = 3.142;
            float UserRadius;
            std::cout << "What's the radius of the circle?\n";
            std::cin >> UserRadius;
            
            float CircleArea;
            
            std::cout << "The area is ";
            std::cout << UserRadius * UserRadius * Pi;
            std::cout << "\n";

        } else if (UserChoice == "n") {
            break;
            
        } else {
            
        }


    }

    


    

    
}