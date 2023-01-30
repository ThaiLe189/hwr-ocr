import { Textarea, TextInput } from "@mantine/core";

type Props = {
    data: any;
};
const handleData = (data: any) => {
    if (data) {
        const rows = [];
        for (let i = 0; i < data.length; i++) {
            // note: we are adding a key prop here to allow react to uniquely identify each
            // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
            rows.push(
                <Textarea
                    label={data[i].Label}
                    description={data[i]?.Pattern}
                    variant="filled"
                    placeholder="Trường này trống"
                    radius="lg"
                    size="md"
                    minRows={1}
                    autosize
                    value={data[i].Text.replace("\n","")}
                />
            );
        }
        return <>{rows}</>;
    }
    return null;

}
 

const TableData = ({ data }: Props) => {
    return <div className="">{handleData(data)}</div>;
};

export default TableData;
