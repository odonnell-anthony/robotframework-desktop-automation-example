*** Settings ***
Documentation     Sikuli Library test
Suite Setup       Start Up
Suite Teardown    Stop Remote Server
Library           SikuliLibrary
Library          ./functions.py



*** Variables ***
${IMAGE_DIR}      ${CURDIR}\\images

*** Tasks ***
Open Paint
    Switch To Desktop
    Start Menu Open
    Wait For Windows Start Menu
    Search For Paint Application
    Select Paint From Start Menu

Open File In Paint
    Click File
    Click Open
    Change Directory
    Open File

Rotate Image in Paint
    Rotate File

Save File and Exit
    Save and Exit



*** Keywords ***
Start Up
    Start Sikuli Process
    Add Image Path    ${IMAGE_DIR}

Switch To Desktop
    Go To Desktop

Start Menu Open
    Open Start Menu

Wait For Windows Start Menu
    Sleep   2      #Just Wait for Windows to open the start menu, can be slow

Search For Paint Application
    Type Paint

Select Paint From Start Menu
    Wait Until Screen Contain       paint_start_menu.png   5
    Click                           paint_start_menu.png

Click File
    Wait Until Screen Contain       paint_file.png   5
    Click                           paint_file.png

Click Open
    Wait Until Screen Contain       paint_open.png   5
    Click                           paint_open.png

Change Directory
    Wait Until Screen Contain       paint_dir.png   5
    Input Text                      paint_dir.png   ${IMAGE_DIR}\\robot
    Press Enter

Open File
    Wait Until Screen Contain       paint_filename.png   5
    Click                           paint_filename.png
    Input Text                      paint_filename.png   robot.png
    Press Enter

Rotate Image
    Wait Until Screen Contain       paint_rotate.png   5
    Click                           paint_rotate.png
    Wait Until Screen Contain       paint_rotate180.png   5
    Click                           paint_rotate180.png

Save and Exit
    Wait Until Screen Contain       paint_save.png   5
    Click                           paint_save.png
    Press Alt F4