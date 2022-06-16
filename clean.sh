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
        sed -i 's/�//g' $f;
        sed -i '1,205 d' $f;
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

    # Remove lines of all numbers
    sed -i 's/^[\s0-9]*$//g' $f;

    # Remove empty lines
    sed -i '/^\s*$/d' $f;

    # Book specific edits
    if [ "$f" == "Descartes.txt" ]; then
        # Loose page numbers and notes
        sed -i 's/\s*[0-9]*$//g' $f;
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
        :
    fi

    if [ "$f" == "Moral_Luck.txt" ]; then
        :
    fi

    if [ "$f" == "Morality.txt" ]; then
        :
    fi

    if [ "$f" == "On_Opera.txt" ]; then
        :
    fi

    if [ "$f" == "Philosophy_as_a_Humanistic_Discipline.txt" ]; then
        :
    fi

    if [ "$f" == "Problems_of_the_Self.txt" ]; then
        :
    fi

    if [ "$f" == "Shame_and_Necessity.txt" ]; then
        :
    fi

    if [ "$f" == "Truth_and_Truthfulness.txt" ]; then
        :
    fi


done