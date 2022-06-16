#!/bin/bash
mkdir -p books/txt_clean

for f in books/txt_og/*.txt; do
    cp "$f" $(echo $f | sed s%txt_og%txt_clean% | sed s%\\s%_%g);
done

cd books/txt_clean;
for f in *.txt; do
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
        sed -i 's%�% %g' $f;
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

done