#!/bin/bash

# Create folder
mkdir -p books/txt_clean

# Copy og
for f in books/txt_og/*.txt; do
    cp "$f" $(echo $f | sed s/txt_og/txt_clean/ | sed 's/\s/_/g');
done

cd books/txt_clean;
for f in *.txt; do

    # Remove head and tail

    if [ "$f" == "Descartes.txt" ]; then
        sed -i '5154,$ d' $f;
        sed -i '1,336 d' $f;
    fi

    if [ "$f" == "Essays_and_Reviews.txt" ]; then
        sed -i '4090,$ d' $f;
        sed -i '1,300 d' $f;
    fi

    if [ "$f" == "Ethics_and_the_Limits_of_Philosophy.txt" ]; then
        sed -i '2058,$ d' $f;
        sed -i '1,182 d' $f;
    fi

    if [ "$f" == "In_the_Beginning_Was_the_Deed.txt" ]; then
        sed -i '1735,$ d' $f;
        sed -i '1,244 d' $f;
    fi

    if [ "$f" == "Moral_Luck.txt" ]; then
        tr -d '\014' < $f > tmp.txt && mv tmp.txt $f;
        sed -i '1,195 d' $f;
    fi

    if [ "$f" == "Morality.txt" ]; then
        tr -d '\014' < $f > tmp.txt && mv tmp.txt $f;
        sed -i '1,166 d' $f;
    fi

    if [ "$f" == "On_Opera.txt" ]; then
        sed -i '3167,$ d' $f;
        sed -i '1,362 d' $f;
    fi

    if [ "$f" == "Philosophy_as_a_Humanistic_Discipline.txt" ]; then
        sed -i '2230,$ d' $f;
        sed -i '1,300 d' $f;
    fi

    if [ "$f" == "Problems_of_the_Self.txt" ]; then
        tr -d '\014' < $f > tmp.txt && mv tmp.txt $f;
        sed -i '11473,$ d' $f;
        sed -i '1,244 d' $f;
    fi

    if [ "$f" == "Shame_and_Necessity.txt" ]; then
        sed -i '4758,$ d' $f;
        sed -i '1,32 d' $f;
    fi

    if [ "$f" == "Truth_and_Truthfulness.txt" ]; then
        sed -i '2565,$ d' $f;
        sed -i '1,210 d' $f;
    fi

    # Remove whitespaces
    sed -i 's/^\s*//g' $f;
    sed -i 's/\s*$//g' $f;
    sed -i 's/\s\+/ /g' $f;

    # Remove lines of all numbers
    sed -i '/^[\s0-9]*$/d' $f;

    # Remove empty lines
    sed -i '/^\s*$/d' $f;

    # Book specific edits
    if [ "$f" == "Descartes.txt" ]; then
        # Loose page numbers and notes
        sed -i 's/\s*[0-9]\+$//g' $f;
        # Chapter titles
        sed -i -z 's/\([a-zA-Z]\)\nd e s c a r t e s\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\nt h e p r o j e c t\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\ncogito and sum\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\nt h e r e a l d i s t i n c t i o n\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\ng o d\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\ne r r o r a n d t h e w i l l\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\nk n o w l e d g e i s p o s s i b l e\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\np h y s i c a l o b j e c t s\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\ns c i e n c e a n d e x p e r i m e n t\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\nm i n d a n d i t s p l a c e i n n a t u r e\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z]\)\na p p e n d i x\n\([a-zA-Z]\)/\1 \2/g' $f;
        #
        sed -i '/^d e s c a r t e s$/d' $f;
        sed -i '/^t h e p r o j e c t$/d' $f;
        sed -i '/^cogito and sum$/d' $f;
        sed -i '/^t h e r e a l d i s t i n c t i o n$/d' $f;
        sed -i '/^g o d$/d' $f;
        sed -i '/^e r r o r a n d t h e w i l l$/d' $f;
        sed -i '/^k n o w l e d g e i s p o s s i b l e$/d' $f;
        sed -i '/^p h y s i c a l o b j e c t s$/d' $f;
        sed -i '/^s c i e n c e a n d e x p e r i m e n t$/d' $f;
        sed -i '/^m i n d a n d i t s p l a c e i n n a t u r e$/d' $f;
        sed -i '/^a p p e n d i x$/d' $f;
        #
        sed -i 's/^m i n d a n d i t s p l a c e i n n a t u r e //g' $f;
      
    fi

    if [ "$f" == "Essays_and_Reviews.txt" ]; then
        :
    fi

    if [ "$f" == "Ethics_and_the_Limits_of_Philosophy.txt" ]; then
        :
    fi

    if [ "$f" == "In_the_Beginning_Was_the_Deed.txt" ]; then
        # Loose page numbers and notes
        sed -i 's/\s*[0-9]\+$//g' $f;
    fi

    if [ "$f" == "Moral_Luck.txt" ]; then
        sed -i '/^[^a-oq-zA-HJ-Z]*$/d' $f;

        sed -i '/^Moral luck/d' $f;
        sed -i '/Persons, character and morality/d' $f;
        sed -i '/Utilitarianism and moral self-indulgence/d' $f;
        sed -i '/Politics and moral character/d' $f;
        sed -i '/Conflicts of values/d' $f;
        sed -i '/Justice as a virtue/d' $f;
        sed -i "/Rawls and Pascal's wager/d" $f;
        sed -i '/Internal and external reasons/d' $f;
        sed -i '/Ought and moral obligation/d' $f;
        sed -i '/Practical necessity/d' $f;
        sed -i '/The truth in relativism/d' $f;
        sed -i '/Wittgenstein and idealism/d' $f;
        sed -i '/Another time, another place, another person/d' $f;
        
        # Anti line wrap
        sed -i -z 's/\([^.!?]\)\n\([^A-Z]\)/\1 \2/g' $f;

        # (!) Notes breaks the flow of the text
    fi

    if [ "$f" == "Morality.txt" ]; then
        sed -i '/^[Pp]age [0-9ivx]\+$/d' $f;
        # Anti-hypenation
        sed -i -z 's/\([a-z]\)-\n\([a-z]\)/\1\2/g' $f;
        # Anti line wrap
        sed -i -z 's/\([^.!?]\)\n\([^A-Z]\)/\1 \2/g' $f;
    fi

    if [ "$f" == "On_Opera.txt" ]; then
        sed -i '/^[0-9]\{2\} Chapter [0-9]\{4\} [0-9]\{2\}\/[0-9]\/[0-9]\{2\} [0-9]\{2\}:[0-9]\{2\} Page [0-9]\+$/d' $f;
        # Loose page numbers and notes
        sed -i 's/\s*[0-9]\+$//g' $f;
        # Chapter titles
        sed -i -z 's/\([a-zA-Z\-]\)\nO N O P E R A\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nT H E N AT U R E O F O P E R A\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nM O Z A RT ’ S C O M E D I E S A N D T H E S E N S E O F A N E N D I N G\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nM O Z A RT ’ S F I G A R O\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nD O N G I O VA N N I A S A N I D E A\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nPA S S I O N A N D C Y N I C I S M\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nR AT H E R R E D T H A N B L A C K\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nT R I S TA N A N D T I M E\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nT H E E L U S I V E N E S S O F P E S S I M I S M\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nWA G N E R A N D T H E T R A N S C E N D E N C E O F P O L I T I C S\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nL’ E N V E R S D E S D E S T I N É E S\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nM A N I F E S T A RT I F I C E\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nC O M M E N T S O N O P E R A A N D I D E A S\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nT H E M A R R I A G E A N D T H E F L U T E\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nJ A N Á CĚ K ’ S M O D E R N I S M\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nA U T H E N T I C I T Y A N D R E - C R E AT I O N\n\([a-zA-Z]\)/\1 \2/g' $f;
        sed -i -z 's/\([a-zA-Z\-]\)\nN A Ï V E A N D S E N T I M E N TA L O P E R A L O V E R S\n\([a-zA-Z]\)/\1 \2/g' $f;
        #
        sed -i '/^O N O P E R A$/d' $f;
        sed -i '/^T H E N AT U R E O F O P E R A$/d' $f;
        sed -i '/^M O Z A RT ’ S C O M E D I E S A N D T H E S E N S E O F A N E N D I N G$/d' $f;
        sed -i '/^M O Z A RT ’ S F I G A R O$/d' $f;
        sed -i '/^D O N G I O VA N N I A S A N I D E A$/d' $f;
        sed -i '/^PA S S I O N A N D C Y N I C I S M$/d' $f;
        sed -i '/^R AT H E R R E D T H A N B L A C K$/d' $f;
        sed -i '/^T R I S TA N A N D T I M E$/d' $f;
        sed -i '/^T H E E L U S I V E N E S S O F P E S S I M I S M$/d' $f;
        sed -i '/^WA G N E R A N D T H E T R A N S C E N D E N C E O F P O L I T I C S$/d' $f;
        sed -i '/^L’ E N V E R S D E S D E S T I N É E S$/d' $f;
        sed -i '/^M A N I F E S T A RT I F I C E$/d' $f;
        sed -i '/^C O M M E N T S O N O P E R A A N D I D E A S$/d' $f;
        sed -i '/^T H E M A R R I A G E A N D T H E F L U T E$/d' $f;
        sed -i '/^J A N Á CĚ K ’ S M O D E R N I S M$/d' $f;
        sed -i '/^A U T H E N T I C I T Y A N D R E - C R E AT I O N$/d' $f;
        sed -i '/^N A Ï V E A N D S E N T I M E N TA L O P E R A L O V E R S$/d' $f;

        # Anti-hypenation
        sed -i -z 's/\([a-z]\)-\n\([a-z]\)/\1\2/g' $f;
        # Anti line wrap
        sed -i -z 's/\([^.!?]\)\n\([^A-Z]\)/\1 \2/g' $f;
    fi

    if [ "$f" == "Philosophy_as_a_Humanistic_Discipline.txt" ]; then
        # Loose page numbers and notes
        sed -i 's/\s*[0-9]\+$//g' $f;
    fi

    if [ "$f" == "Problems_of_the_Self.txt" ]; then

        # Chapter titles
        sed -i '/^Problems of the Self$/d' $f;
        sed -i '/^Personal identity and individuation$/d' $f;
        sed -i '/^Bodily continuity and personal identity$/d' $f;
        sed -i '/^Imagination and the self$/d' $f;
        sed -i '/^The self and the future$/d' $f;
        sed -i '/^Are persons bodies?$/d' $f;
        sed -i '/^The Makropulos case: reflections on the tedium of immortality$/d' $f;
        sed -i '/^Strawson on individuals$/d' $f;
        sed -i '/^Knowledge and meaning in the philosophy of mind$/d' $f;
        sed -i '/^Deciding to believe$/d' $f;
        sed -i '/^Imperative inference$/d' $f;
        sed -i '/^Additional note (1972)$/d' $f;
        sed -i '/^Ethical consistency$/d' $f;
        sed -i '/^Consistency and realism$/d' $f;
        sed -i '/^Morality and the emotions$/d' $f;
        sed -i '/^The idea of equality$/d' $f;
        sed -i '/^Egoism and altruism$/d' $f;

        # Anti-hypenation
        sed -i -z 's/\([a-z]\)-\n\([a-z]\)/\1\2/g' $f;
        # Anti line wrap
        sed -i -z 's/\([^.!?]\)\n\([^A-Z]\)/\1 \2/g' $f;

        # Loose page numbers and notes
        sed -i 's/\s*[0-9]\+\s*$//g' $f;

        # (!) Notes breaks the flow of the text
    fi

    if [ "$f" == "Shame_and_Necessity.txt" ]; then
        sed -i '/^http/d' $f;
        sed -i '/^[― 0-9ixv]*$/d' $f;
        sed -i '/^11\/13\/2007 9\:45 PM$/d' $f;
        sed -i '/^[0-9]\+ of [0-9]\+$/d' $f;
        sed -i '/^Shame and Necessity$/d' $f;
        sed -i 's/\[[0-9]\+\]//g' $f;

        # Anti-hypenation
        sed -i -z 's/\([a-z]\)-\n\([a-z]\)/\1\2/g' $f;
        # Anti line wrap
        sed -i -z 's/\([^.!?]\)\n\([^A-Z]\)/\1 \2/g' $f;
    fi

    if [ "$f" == "Truth_and_Truthfulness.txt" ]; then
        :
    fi

done

zip txt_clean.zip *.txt