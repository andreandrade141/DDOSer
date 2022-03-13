# LOGGER.PY DOCUMENTATION

## Description

This module is responsible for logging all projects operations. the log structure goes as following:

URL: XXXXXXXXXX
STATUS CODE: XXX
RESULT: (XXXX) - XXXXXXXXXXX
TOTAL TIME: XXXXXX
EXECUTION DATE: XXXXXXXX

- The URL field will display the tested link.

- The STATUS code field will output the HTTP code of the request.W(If there's an error prior to the request the code will appear as 0).

- The RESULT field will output the status of the operation (DONE or FAIL) and a small description of it´s procedures.

- The TOTAL TIME field will output the total time that took to execute the request module.

- The EXECUTION DATE will output the datetime of the execution.

## Module Logic

1. The module controller will receive the log input and send it to one of two functions -> faillog or successlog.

2. The two works the same way, by treating the information and preformatting it before sending it to the logwriter function

3. The logwriter function is responsible for formatting all the info and showing it in the format mentioned above.
