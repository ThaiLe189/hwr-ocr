import { Button, Group, Image, Loader, Stack, Tabs, Text } from "@mantine/core";
import { Dropzone, IMAGE_MIME_TYPE } from "@mantine/dropzone";
import { useEffect, useState } from "react";
import axiosClient from "../utils/apis/RequestHelper";
import { _IApiResponse } from "../utils/interfaces/IApiResponse";
import TableData from "./tabledata";

interface Idata {
    ImageBase64: string;
}

const Home = () => {
    const [imageData, setImageData] = useState<null | string>(null);
    const loadFile = (file: File) => {
        const reader = new FileReader();
        reader.onloadend = () => {
            const imageDataUri = reader.result;
            setImageData(imageDataUri as string);
        };
        reader.readAsDataURL(file);
        setNoClick(false);
    };

    const [ocrResult, setOcrResult] = useState("");
    const [loading, setLoading] = useState(false);
    const [res, setRes] = useState();
    const [noClick, setNoClick] = useState(false);
    useEffect(() => {}, []);

    const post = async (path: string, data: Idata): Promise<_IApiResponse> => {
        return axiosClient.post(`/api/${path}`, data);
    };

    const handleExtract = async (endpoint: string) => {
        setLoading(true);
        try {
            let imgBase64 = imageData as string;
            const response = await post(endpoint, {
                ImageBase64: imgBase64.replace(
                    /^data:image\/[a-z]+;base64,/,
                    ""
                ),
            });
            setOcrResult(response.body?.text || "");
            setRes(response.body?.res || "");
            setImageData("data:image/jpeg;base64," + response.body.imagebase64);
            setNoClick(true);
        } catch (error) {
            console.log(error);
        }
        setLoading(false);
    };

    return (
        <div className="">
            <Group align="initial" style={{ padding: "10px" }}>
                <Stack style={{ flex: "1" }}>
                    <Dropzone
                        onDrop={(files) => loadFile(files[0])}
                        accept={IMAGE_MIME_TYPE}
                        multiple={false}
                    >
                        {() => (
                            <Text
                                size="xl"
                                inline
                                style={{ textAlign: "center" }}
                            >
                                Kéo hình ảnh vào đây hoặc bấm để chọn tập tin
                            </Text>
                        )}
                    </Dropzone>

                    {!!imageData && (
                        <Image src={imageData} style={{ width: "100%" }} />
                    )}
                </Stack>

                <Stack style={{ flex: "1" }}>
                    <div className="flex gap-11">
                        <Button
                            disabled={noClick}
                            onClick={() => handleExtract("img2text/cvt")}
                            className="bg-blue-500"
                            loading={loading}
                        >
                            Nhận dạng chữ in
                        </Button>

                        <Button
                            disabled={noClick}
                            onClick={() => handleExtract("cv")}
                            className="bg-blue-500"
                            loading={loading}
                        >
                            Bóc tách thông tin CV
                        </Button>
                        <Button
                            disabled={noClick}
                            onClick={() => handleExtract("cccd")}
                            className="bg-blue-500"
                            loading={loading}
                        >
                            Bóc tách thông tin CCCD
                        </Button>
                    </div>

                    {/* <Text>{progressLabel.toUpperCase()}</Text>
                    <Progress value={progress * 100} /> */}

                    <Stack>
                        <>
                            <Tabs variant="outline" tabPadding="sm">
                                <Tabs.Tab
                                    label="Kết quả nhận dạng"
                                    disabled={ocrResult == ""}
                                >
                                    {loading ? (
                                        <div className="flex justify-center">
                                            <Loader size={100} variant="dots" />
                                        </div>
                                    ) : (
                                        <Text
                                            style={{
                                                fontFamily: "monospace",
                                                background: "gray",
                                                padding: "10px",
                                                whiteSpace: "pre-line",
                                            }}
                                        >
                                            {ocrResult}
                                        </Text>
                                    )}
                                </Tabs.Tab>
                                <Tabs.Tab
                                    label="Kết quả bóc tách"
                                    disabled={res === undefined || res === ""}
                                >
                                    {loading ? (
                                        <div className="flex justify-center">
                                            <Loader size={100} variant="dots" />
                                        </div>
                                    ) : (
                                        <div className="px-5">
                                            <TableData data={res} />
                                        </div>
                                    )}
                                </Tabs.Tab>
                            </Tabs>
                        </>
                    </Stack>
                </Stack>
            </Group>
        </div>
    );
};

export default Home;
