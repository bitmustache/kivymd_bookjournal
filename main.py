from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
import uuid


class BookJournal(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alldata = []
        self.mydialog = None

    def build(self):
        self.screen = Builder.load_file("load.kv")
        self.theme_cls.primary_palette = "Orange"
        return self.screen
    
    #create function for adding book category
    def addnewbookcategory(self, value):
        print(value)
        if value: 
            #create uuid for edit and delete
            item_id = str(uuid.uuid4())
            self.alldata.append(
                {"value": value, "id": item_id}
            )

            #get id from kv file mdlist
            bookcategorylist = self.screen.ids.bookcategorylist
            
            #add to widget in bookcategorylist selector
            bookcategorylist.add_widget(
                OneLineAvatarIconListItem(
                    IconLeftWidget(
                        icon = "pencil",
                        on_release = lambda x:self.editbtn(item_id, value)
                    ),
                    IconRightWidget(
                        icon = "delete",
                        on_release = lambda x:self.deletebtn(item_id)
                    ),
                    id = item_id,
                    text = value
                )
            )

           #adjust the height of the list to fit the new item
            bookcategorylist.height = sum([child.height for child in bookcategorylist.children])

        #clear input text after clicking add button
        self.screen.ids.inputbookcategory.text = ""
    
    def editbtn(self, dataid, value):
        pass

    def deletebtn(self, data):
        #loop self.alldata and check if id == data and remove
        for x in self.alldata:
            if x['id'] == data:
                self.alldata.remove(x)
                print(self.alldata)

                bookcategorylist = self.screen.ids.bookcategorylist
                for child in bookcategorylist.children:
                    if child.id == data:
                        bookcategorylist.remove_widget(child)



app = BookJournal()
app.run()
