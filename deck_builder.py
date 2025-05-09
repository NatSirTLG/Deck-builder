
import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as tkfont

# Données des cartes
familles = {
    "Machina": {
        "Légendaires": ["Mecha Titan", "Cyber Dragon"],
        "Rares": [f"Machina R{i}" for i in range(1, 14)]
    },
    "Evil": {
        "Légendaires": ["Dark Overlord", "Demon King"],
        "Rares": [f"Evil R{i}" for i in range(1, 14)]
    },
    "Legends": {
        "Légendaires": ["Arthur", "Zeus"],
        "Rares": [f"Legends R{i}" for i in range(1, 14)]
    }
}

class DeckBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AetherBorn: Deck Builder")
        self.root.geometry("800x900")  # Increased window size
        self.root.resizable(False, False)  # Prevent window resizing
        self.root.configure(bg='#2C3E50')  # Dark background

        # Custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=14)

        self.famille_choisie = tk.StringVar(value="")
        self.deck = []
        self.deck_started = False

        self.setup_interface()

    def setup_interface(self):
        # Main frame to hold all content
        self.main_frame = tk.Frame(self.root, bg='#2C3E50', width=760, height=850)
        self.main_frame.pack(fill=tk.BOTH, expand=False, padx=20, pady=20)
        self.main_frame.pack_propagate(False)  # Prevent frame from resizing

        # Title
        title_label = tk.Label(self.main_frame, text="AetherBorn Deck Builder", 
                               font=self.title_font, fg='white', bg='#2C3E50')
        title_label.pack(pady=(0, 20), anchor='center')

        # Family Selection Frame
        family_selection_frame = tk.Frame(self.main_frame, bg='#2C3E50', height=70)
        family_selection_frame.pack(pady=10, fill=tk.X)
        family_selection_frame.pack_propagate(False)  # Prevent frame from resizing

        # Family Selection Label
        family_label = tk.Label(family_selection_frame, text="Choisissez la famille de votre deck :", 
                                font=self.label_font, fg='white', bg='#2C3E50')
        family_label.pack(side=tk.LEFT, padx=(0, 10))

        # Family Selection Dropdown
        family_dropdown = ttk.Combobox(family_selection_frame, textvariable=self.famille_choisie, 
                                       values=list(familles.keys()), state="readonly", width=20, font=self.label_font)
        family_dropdown.pack(side=tk.LEFT)

        # Start Deck Button
        start_deck_button = tk.Button(family_selection_frame, text="Commencer le deck", 
                                      command=self.start_deck, bg='#34495E', fg='white', font=self.label_font)
        start_deck_button.pack(side=tk.LEFT, padx=(10, 0))

        # Main content area
        self.content_frame = tk.Frame(self.main_frame, bg='#2C3E50', width=760, height=700)
        self.content_frame.pack(fill=tk.BOTH, expand=False)
        self.content_frame.pack_propagate(False)  # Prevent frame from resizing

    def start_deck(self):
        # Check if a family is selected
        if not self.famille_choisie.get():
            messagebox.showerror("Erreur", "Veuillez sélectionner une famille de cartes!", icon=messagebox.ERROR)
            return
        
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Mark deck as started
        self.deck_started = True
        self.deck = []

        # Create a frame to hold the deck builder interface
        deck_frame = tk.Frame(self.content_frame, bg='#2C3E50', width=760, height=700)
        deck_frame.pack(fill=tk.BOTH, expand=False)
        deck_frame.pack_propagate(False)  # Prevent frame from resizing

        # Left side: Family and Cards
        left_frame = tk.Frame(deck_frame, bg='#2C3E50', width=370, height=650)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10)
        left_frame.pack_propagate(False)  # Prevent frame from resizing

        # Right side: Deck Display
        right_frame = tk.Frame(deck_frame, bg='#2C3E50', width=370, height=650)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=10)
        right_frame.pack_propagate(False)  # Prevent frame from resizing

        # Deck Stats Label
        self.deck_stats_label = tk.Label(left_frame, text="0/15 Cards", 
                                         font=self.label_font, fg='white', bg='#2C3E50')
        self.deck_stats_label.pack(pady=(0, 10))

        # Create the rest of the interface
        self.create_card_list(left_frame)
        self.create_deck_display(right_frame)

        # Populate card list for the selected family
        famille = self.famille_choisie.get()
        
        # Clear existing items
        self.cartes_listbox.delete(0, tk.END)
        
        # Add Legendary cards
        if familles[famille]["Légendaires"]:
            self.cartes_listbox.insert(tk.END, "--- Legendary Cards ---")
            for carte in familles[famille]["Légendaires"]:
                self.cartes_listbox.insert(tk.END, f"{carte} (Legendary)")
        
        # Add Rare cards
        if familles[famille]["Rares"]:
            self.cartes_listbox.insert(tk.END, "--- Rare Cards ---")
            for carte in familles[famille]["Rares"]:
                self.cartes_listbox.insert(tk.END, f"{carte} (Rare)")

        # Reset Button
        reset_button_style = {'font': self.label_font, 'bg': '#E74C3C', 'fg': 'white', 'activebackground': '#C0392B'}
        reset_button = tk.Button(deck_frame, text="Reset", command=self.reset, **reset_button_style)
        reset_button.pack(side=tk.BOTTOM, pady=10)

    def create_card_list(self, parent_frame):
        # Cartes Listbox Frame
        cartes_frame = tk.Frame(parent_frame, bg='#2C3E50')
        cartes_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbar for Cartes Listbox
        cartes_scrollbar = tk.Scrollbar(cartes_frame)
        cartes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Cards listbox with scrollbar
        listbox_frame = tk.Frame(parent_frame, bg='#2C3E50')
        listbox_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cartes_listbox = tk.Listbox(listbox_frame, 
                                         selectmode=tk.SINGLE, 
                                         width=50, 
                                         height=10,
                                         font=self.label_font,
                                         yscrollcommand=scrollbar.set,
                                         bg='#34495E', 
                                         fg='white')
        self.cartes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.cartes_listbox.yview)

        # Bind double-click event to add card
        self.cartes_listbox.bind('<Double-1>', self.ajouter_au_deck)



    def ajouter_au_deck(self, event=None):
        # Check if deck has been started
        if not self.deck_started:
            messagebox.showerror("Erreur", "Veuillez d'abord commencer un deck!", icon=messagebox.ERROR)
            return

        # If called from double-click, get selected card from event
        if event:
            selection = self.cartes_listbox.curselection()
        else:
            selection = self.cartes_listbox.curselection()

        # Validate selection
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner une carte!", icon=messagebox.ERROR)
            return

        # Get the selected card
        selected_index = selection[0]
        selected_card = self.cartes_listbox.get(selected_index)

        # Deck rules
        if len(self.deck) >= 15:
            messagebox.showerror("Deck Full", "Your deck can only contain 15 cards!", icon=messagebox.ERROR)
            return

        # Check if card is a header
        if selected_card.startswith("---"):
            messagebox.showerror("Erreur", "Vous ne pouvez pas ajouter un en-tête!", icon=messagebox.ERROR)
            return

        # Remove the rarity info
        if " (" in selected_card:
            selected_card = selected_card.split(" (")[0]

        # Determine the card type (Legendary or Rare)
        card_type = "Rare" if "(Rare)" in self.cartes_listbox.get(selected_index) else "Legendary"
        
        # Check if the card is a Legendary card
        is_legendary = any(selected_card in family_data.get("Légendaires", []) for family_data in familles.values())
        
        # Strict card limit rules
        card_counts = {}
        legendary_count = 0
        for card in self.deck:
            card_counts[card] = card_counts.get(card, 0) + 1
            
            # Check if card is legendary
            for family_data in familles.values():
                if card in family_data.get("Légendaires", []):
                    legendary_count += 1
        
        # Limit each card to 2 copies
        if card_counts.get(selected_card, 0) >= 2:
            messagebox.showerror("Limit Reached", f"You can only have 2 copies of {selected_card} in a deck!", icon=messagebox.ERROR)
            return
        
        # Limit legendary cards to 2 across ALL families
        if is_legendary:
            if legendary_count >= 2:
                messagebox.showerror("Legendary Limit", "You can only have 2 Legendary cards in a deck!", icon=messagebox.ERROR)
                return
        
        # Add card to deck
        self.deck.append(selected_card)
        self.deck_stats_label.config(text=f"{len(self.deck)}/15 Cards")

        # Update deck display (this will handle listbox and stats label)
        self.update_deck_display()

    def retirer_du_deck(self, event=None):
        # Get the selected card
        selection = self.deck_listbox.curselection()
        if not selection:
            return

        # Get the selected card text
        selected_item = self.deck_listbox.get(selection[0])
        
        # Extract the card name (remove the count)
        selected_card = selected_item.split(" (x")[0] if " (x" in selected_item else selected_item

        # Remove the first occurrence of the card from the deck
        if selected_card in self.deck:
            self.deck.remove(selected_card)

            # Update the deck display
            self.update_deck_display()

    def update_deck_display(self):
        # Clear previous deck display
        self.deck_listbox.delete(0, tk.END)

        # Count cards in the deck
        card_counts = {}
        for carte in self.deck:
            card_counts[carte] = card_counts.get(carte, 0) + 1

        # Determine card types
        legendary_cards = set()
        rare_cards = set()
        for family_data in familles.values():
            legendary_cards.update(family_data.get("Légendaires", []))
            rare_cards.update(family_data.get("Rares", []))

        # Display cards with their counts and colors
        for card, count in sorted(card_counts.items(), key=lambda x: x[0]):
            self.deck_listbox.insert(tk.END, f"{card} (x{count})")
            
            # Color the card based on its type
            if card in legendary_cards:
                self.deck_listbox.itemconfig(tk.END, {'fg': '#FF5733'})
            elif card in rare_cards:
                self.deck_listbox.itemconfig(tk.END, {'fg': '#33d7ff'})

        # Update deck stats label
        self.deck_stats_label.config(text=f"{len(self.deck)}/15 Cards")

    def create_card_list(self, parent_frame):
        # Cartes Listbox Frame
        cartes_frame = tk.Frame(parent_frame, bg='#2C3E50', width=370, height=600)
        cartes_frame.pack(fill=tk.BOTH, expand=False)
        cartes_frame.pack_propagate(False)  # Prevent frame from resizing

        # Family Selection
        famille_label = tk.Label(cartes_frame, text=f"Famille : {self.famille_choisie.get()}", 
                                 font=self.label_font, fg='white', bg='#2C3E50')
        famille_label.pack(pady=(10, 10))

        # Cards listbox
        self.cartes_listbox = tk.Listbox(cartes_frame, 
                                         selectmode=tk.SINGLE, 
                                         width=50, 
                                         height=25,
                                         font=self.label_font,
                                         bg='#34495E')
        self.cartes_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=10)

        # Bind double-click event to add card
        self.cartes_listbox.bind('<Double-1>', self.ajouter_au_deck)
        
        # Add cards with appropriate colors
        famille = self.famille_choisie.get()
        
        # Add Legendary cards
        if familles[famille]["Légendaires"]:
            self.cartes_listbox.insert(tk.END, "--- Legendary Cards ---")
            for carte in familles[famille]["Légendaires"]:
                self.cartes_listbox.insert(tk.END, f"{carte} (Legendary)")
                self.cartes_listbox.itemconfig(tk.END, {'fg': '#FF5733'})
        
        # Add Rare cards
        if familles[famille]["Rares"]:
            self.cartes_listbox.insert(tk.END, "--- Rare Cards ---")
            for carte in familles[famille]["Rares"]:
                self.cartes_listbox.insert(tk.END, f"{carte} (Rare)")
                self.cartes_listbox.itemconfig(tk.END, {'fg': '#33d7ff'})
        
        # Color headers white
        for i in range(self.cartes_listbox.size()):
            item = self.cartes_listbox.get(i)
            if item.startswith("---"):
                self.cartes_listbox.itemconfig(i, {'fg': 'white'})

    def create_deck_display(self, parent_frame):
        # Deck Display Frame
        deck_frame = tk.Frame(parent_frame, bg='#2C3E50', width=370, height=600)
        deck_frame.pack(fill=tk.BOTH, expand=False)
        deck_frame.pack_propagate(False)  # Prevent frame from resizing

        # Deck Title
        deck_title = tk.Label(deck_frame, text="Current Deck", 
                              font=self.label_font, fg='white', bg='#2C3E50')
        deck_title.pack(pady=(10, 5))

        # Deck Listbox
        self.deck_listbox = tk.Listbox(deck_frame, 
                                       selectmode=tk.SINGLE, 
                                       width=50, 
                                       height=25,
                                       font=self.label_font,
                                       bg='#34495E', 
                                       fg='white')
        self.deck_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=10)

        # Bind double-click event to remove card
        self.deck_listbox.bind('<Double-1>', self.retirer_du_deck)

        # Deck stats label
        self.deck_stats_label = tk.Label(deck_frame, 
                                         text="Cards: 0/15", 
                                         font=self.label_font, 
                                         fg='white', 
                                         bg='#2C3E50')
        self.deck_stats_label.pack(pady=(5, 10))

    def afficher_deck(self):
        if not self.deck:
            messagebox.showinfo("Deck", "Your deck is empty!", icon=messagebox.INFO)
        else:
            contenu = "\n".join(f"{carte} (x{self.deck.count(carte)})" for carte in set(self.deck))
            messagebox.showinfo("Ton deck", f"Cartes dans ton deck ({len(self.deck)} / 15):\n\n{contenu}")

    def reset(self):
        # Reset deck and restart the deck building process
        self.deck = []
        self.deck_started = False
        
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Recreate the entire interface
        self.setup_interface()
        
        messagebox.showinfo("Réinitialisé", "Ton deck a été réinitialisé. Choisis une nouvelle famille.")

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = DeckBuilderApp(root)
    root.mainloop()
