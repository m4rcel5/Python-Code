from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfrw import PdfReader, PdfWriter, PageMerge
import os
import time
import comtypes.client

"""
    @author: m4rcel5
    15.09.2022
    PDFToolkit
"""

# Hier werden die Metadaten eines PDF Dokuments ausgelesen
# IN: path (str, Der Pfad zu einem PDF Dokument)
# OUT: ---
def read_meta(path):
    try:

        with open(path, "rb") as file:
            pdf = PdfFileReader(file)
            meta = pdf.getDocumentInfo()
            pages = pdf.getNumPages()
            os.system("cls")
            for key in meta:
                print(f"{key.lstrip('/')} => {meta[key]}")
            print(f"Amount of pages => {pages}")
            print()
    except:
        print("An unexpected error occurred during this process")
    return


# Hier werden die Metadaten eines PDF Dokuments gelöscht
# IN: pdf_path (str, Der Pfad zu einem PDF Dokument)
# OUT: ---
def delte_meta(pdf_path):
    try:   
        filename = pdf_path.split("\\")[-1]    
        path = pdf_path.replace(filename, "")
        writer = PdfFileWriter()    
        tmp = f"{path}tmp.{filename}"

        with open(tmp, "wb") as new_file:
            with open(pdf_path, "rb") as file:
                pdf = PdfFileReader(file)
                for page in range(pdf.getNumPages()):
                    writer.addPage(pdf.getPage(page))
                    writer.write(new_file)
        os.remove(pdf_path)
        os.rename(tmp, path + filename)
        os.system("cls")
        print(f"Successfull removed meta data from {filename}")

    except Exception:
        print("An unexpected error occurred during this process")
    return


# Hier können die Metadaten eines PDF Dokuments beliebig vom Benutzer manipuliert werden
# IN: pdf_path (str, Der Pfad zu einem PDF Dokument), metadata (dict, Die zu übernehmenden Metadaten)
# OUT: ---
def write_meta(pdf_path, metadata):
    try:   
        filename = pdf_path.split("\\")[-1]    
        path = pdf_path.replace(filename, "")
        writer = PdfFileWriter()    
        tmp = f"{path}tmp.{filename}"

        with open(tmp, "wb") as new_file:
            with open(pdf_path, "rb") as file:
                pdf = PdfFileReader(file)
                for page in range(pdf.getNumPages()):
                    writer.addPage(pdf.getPage(page))
                    writer.write(new_file)
                writer.addMetadata(metadata)
                writer.write(new_file)

        os.remove(pdf_path)
        os.rename(tmp, path + filename)
        os.system("cls")
        print(f"Successfull manipulated meta data from {filename}")

    except Exception:
        print("An unexpected error occurred during this process")
    return


# Hier wird ein PDF Dokument verschlüsselt
# IN: path (str, Der Pfad zu einem PDF Dokument)
# OUT: ---
def encrypt_pdf(path):
    try:
        pdf_reader = PdfFileReader(path)
        pdf_writer = PdfFileWriter()
        filename = path.split("\\")[-1]
        correct = False

        while not correct:
            password = input("Enter your password: ")
            password_retype = input("Retype your password: ")
            if(password == password_retype):
                correct = True
            else:
                os.system("cls")
                print("Passwords not equal!")
                time.sleep(3)
                os.system("cls")
                print("Try it again")
                time.sleep(2)
                os.system("cls")
                
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, use_128bit=True)

        with open(path + "_encrypted.pdf", "wb") as file:
            pdf_writer.write(file)
        os.system("cls")
        print(f"{filename} was successfully encrypted")
    except Exception:
        print("An unexpected error occurred during this process")
    return


# Hier wird ein Wasserzeichen zu einem PDF Dokument hinzugefügt
# IN: pdf_path (str, Der Pfad zum PDF Dokument welches mit dem Wasserzeichen versehen werden soll), logo_path (str, Der Pfad zum Wasserzeichen Logo)
# OUT: ---
def watermark(pdf_path, logo_path):
    try:
        pdf = PdfReader(pdf_path)
        logo = PdfReader(logo_path)
        watermark = logo.pages[0]
        pageNumber = len(pdf.pages)

        for page in range(pageNumber):
            merger = PageMerge(pdf.pages[page])
            merger.add(watermark).render()

        writer = PdfWriter()
        writer.write(pdf_path + "_watermark.pdf", pdf)
        os.system("cls")
        print("Added watermark")
    except Exception:
        print("An unexpected error occurred during this process")
    return


# Hier werden mehrere PDF Dokumente zusammengefügt
# IN: res_name (str, Der Dateiname des Endprodukts )
# OUT: ---
def merge_pdf(res_name):
    try:
        writer = PdfFileWriter()
        count = 0
        pdf_lst = []
        print(f"{count} merged pdf's")

        doc = input("Enter the path to the PDF (empty input to stop): ")
        while doc != "":
            count += 1
            pdf_lst.append(doc)
            print(f"{count} merged pdf's")
            doc = input("Enter the path to the PDF (empty input to stop): ")

        for file in pdf_lst:
            reader = PdfFileReader((file.lstrip('"')).strip('"'))
            for page in range(reader.getNumPages()):
                writer.addPage(reader.getPage(page))

        os.system("cls")        
        with open((res_name.lstrip('"')).strip('"') + ".pdf", "wb") as file:
            writer.write(file)
            print("PDF-File created successfully")
    except Exception:
        print("An unexpected error occurred during this process")
    return


# Hier wird eine .docx Datei in ein PDF Dokument konvertiert
# IN: path (str, Der Pfad zur .docx Datei), final_path (str, Der Pfad in dem das Endprodukt gespeichert werden soll)
# OUT: ---
def word_to_pdf(path, final_path):
    try:
        pdf_format_key = 17
        file_in = os.path.abspath((path.lstrip('"')).strip('"'))
        file_out = os.path.abspath((final_path.lstrip('"')).strip('"'))
        worddoc = comtypes.client.CreateObject( 'Word.Application' )
        doc = worddoc.Documents.Open(file_in)
        doc.SaveAs(file_out, FileFormat = pdf_format_key)
        doc.close()
        worddoc.quit()
        os.system("cls")
        print(f"File converted successfully and saved in {final_path}")
    except Exception:
        print("An unexpected error occurred during this process")
    return


# Ein Menü das dem Benutzer ermöglicht verschiedene Funktionalitäten für PDF Dokumente zu verwenden
def menu():
    while True:
        print("[1] Read Meta Data from a PDF\n"
              "[2] Delete Meta Data from a PDF\n"
              "[3] Manipulate Meta Data from a PDF\n"
              "[4] Encrypt PDF\n"
              "[5] Add watermark to PDF\n"
              "[6] Merge multiple PDF's\n"
              "[7] convert .docx to PDF\n"
              "[0] Stop the program")
        option = int(input(":> "))
        
        if option == 1:
            os.system("cls")
            path = input("Enter the path to the PDF File: ")
            path = (path.lstrip('"')).strip('"')
            read_meta(path)

        elif option == 2:
            os.system("cls")
            path = input("Enter the path to the PDF File: ")
            path = (path.lstrip('"')).strip('"')
            delte_meta(path)

        elif option == 3:
            os.system("cls")
            path = input("Enter the path to the PDF File: ")            
            path = (path.lstrip('"')).strip('"')

            title = input("Enter the title: ")
            subject = input("Enter the subject: ")
            author = input("Enter the author here: ")
            creator = input("Enter the creator here: ")
            producer = input("Enter the producer: ")

            creation_date = input("Enter the creation date (format: dd.mm.yyyy): ").split(".")
            creation_time = input("Enter the creation time (hh:mm:ss): ").split(":")
            c_date = ""

            for datetime in creation_date:
                c_date = datetime + c_date
            for time in creation_time:
                c_date = c_date + time

            mod_date = input("Enter the mod date (format: dd.mm.yyyy): ").split(".")
            mod_time = input("Enter the mod time (hh:mm:ss): ").split(":")
            m_date = ""

            for datetime in mod_date:
                m_date = datetime + m_date
            for time in mod_time:
                m_date = m_date + time            
                
            c_date = "D:" + c_date
            m_date = "D:" + m_date            
            timez = input("Enter your time zone (format: +XX, -XX): ")
            c_date = c_date + timez + "'00'"
            m_date = m_date + timez + "'00'"
            
            metadata = {"/Title" : title,
                        "/Subject" : subject,
                        "/Author" : author,
                        "/Creator" : creator,
                        "/Producer" : producer,
                        "/CreationDate" : c_date,
                        "/ModDate" : m_date}
            write_meta(path, metadata)

        elif option == 4:
            os.system("cls")
            path = input("Enter the path to the PDF File: ")
            path = (path.lstrip('"')).strip('"')
            encrypt_pdf(path)

        elif option == 5:
            os.system("cls")
            path = input("Enter the path to the PDF File: ")
            path = (path.lstrip('"')).strip('"')
            logo_path = input("Enter the path to the watermark logo: ")
            logo_path = (logo_path.lstrip('"')).strip('"')
            watermark(path, logo_path)

        elif option == 6:
            os.system("cls")
            res_name = input("Enter the path with the final file name: ")
            merge_pdf(res_name)

        elif option == 7:
            os.system("cls")
            path = input("Enter the path to the .docx File: ")
            res_name = input("Enter the path with the final file name: ")
            word_to_pdf(path, res_name)

        elif option == 0:
            break

        else:
            os.system("cls")
            print("invalid option")
    return


# ================================================================== MAIN ============================================================================
os.system("cls")
menu()
